# Projeto de Transfer Learning em Python

## Escopo
- O projeto consiste em aplicar o método de Transfer Learning em uma rede de Deep Learning na linguagem Python no ambiente COLAB.
- O dataset utilizado engloba duas classes: gatos e cachorros, cuja descrição da base de dados pode ser obtida [AQUI](https://www.tensorflow.org/datasets/catalog/cats_vs_dogs).
- O dataset pode ser obtido [AQUI](https://www.microsoft.com/en-us/download/details.aspx?id=54765)

## Considerações
Foram necessárias algumas adequações a partir do arquivo do projeto que realiza Transfer Learning com o Dataset do MNIST e que pode ser acessado [AQUI](https://colab.research.google.com/github/kylemath/ml4a-guides/blob/master/notebooks/transfer-learning.ipynb).

Com base nesse dataset foi feita uma amostragem com 200 elementos para prosseguir com o projeto.


### As alterações:
- No tópico 'Getting a dataset' foi necessário substituir a base de dados contendo as imagens anterior para o dataset de gatos e cachorroes que será utilizado nesse projeto.
- Foi necessário reestruturar o dataset conforme o dataset anterior para coincidir a arquitetura de código
- Adequadas as sintaxes de alguns comandos, dentre eles algumas funções de extração, tratamento desses dados.
- Ao início do código foram importados os módulos 'load_img' e 'img_to_array' da biblioteca 'keras.utils' que não estavam contemplados no arquivo original.
- Alterada a helper function get_image(path) conforme a seguir:
~~~
def get_image(path):
    img = load_img(path, target_size=(224, 224))
    x = img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)
    return img, x
~~~
