from PIL import Image
from files import in_file, out_file

def greyscale(colored):
    w, h = colored.size
    img = Image.new("RGB", (w, h))

    for i in range(w):
        for j in range(h):
            pxl = colored.getpixel((i, j))
            # coordenadas RGP considerando a percepção humana em:
            # 30% para vermelho, 59% para verde e 11% para azul
            lum = int(0.3*pxl[0] + 0.59*pxl[1] + 0.11*pxl[2])
            img.putpixel((i, j), (lum, lum, lum))
    return img

def binary(colored):
    w, h = colored.size
    img = Image.new("RGB", (w, h))

    for i in range(w):
        for j in range(h):
            pxl = colored.getpixel((i, j))
            # média das coordenadas RGP
            lum = (pxl[0] + pxl[1] + pxl[2])//3
            bin_lum = 0 if lum < 110 else 255
            img.putpixel((i, j), (bin_lum, bin_lum, bin_lum))
    return img   

if __name__ == "__main__":
    input_file = 'lena.jpg'
    grey_file = 'lenagrey.jpg'
    binary_file = 'lenabin.jpg'

    # Greyscale
    picture = Image.open(in_file(input_file))
    grey_image = greyscale(picture)
    grey_image.save(out_file(grey_file))

    # Black and White
    picture = Image.open(in_file(input_file))
    bin_image = binary(picture)
    bin_image.save(out_file(binary_file))