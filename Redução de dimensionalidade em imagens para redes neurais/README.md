# Redução de Dimensionalidade em Imagens para Redes Neurais

Objetivo: Trazer uma implementação em Python para transformar uma imagem colorida para uma imagem em níveis de cinza e para uma imagem binarizada em preto e branco.

Para a imagem em níveis de cinza foi considerada a sensibilidade do olho humano para as cores primárias: 30% para vermelho, 59% para verde e 11% para azul, no espectro RGB.

Para a imagem binarizada em preto e branco foi considerada a luminância de cada pixel, sendo o branco definido para valores entre 111 e 255, e preto para valores entre 0 e 110.