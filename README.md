# my-py-package

> Criação de um processador, em python, para implementar o ciclo de desenvolvimento de pacotes.

## Sobre o Projeto

img_processing é um projeto didático em Python com foco em ensinar como criar, organizar, empacotar e publicar um pacote na PyPI. O objetivo não é apenas processar imagens, mas mostrar na prática como funciona o ciclo completo de desenvolvimento de um pacote Python — desde a estruturação até a publicação.

Este projeto foi criado com três objetivos principais:

1. Entender conceitos relacionados à criação de pacotes Python

2. Atualizar o projeto e gerar distribuições

3. Publicar o pacote no PyPI

## Funcionalidades

Apesar de simples, o pacote possui funcionalidades reais de processamento de imagens, implementadas com orientação a objetos:

- Combinação de imagens: junta duas imagens lado a lado.

- Transformações: aplica rotação, espelhamento e redimensionamento.

- Conversões: transforma imagens em arrays `NumPy` e vice-versa.

- Visualização e salvamento: exibe imagens com `matplotlib` e salva com `Pillow`.

## Estrutura do Projeto

```bash
img_processing/
├── processing/
│   ├── combination.py       # Combina imagens
│   ├── transformation.py    # Aplica transformações
├── utils/
│   ├── to.py                # Conversões de formato
│   ├── plot.py              # Exibição e salvamento
├── __init__.py              # Inicialização do pacote
├── README.md                # Documentação do projeto
├── setup.py                 # Configuração para empacotamento
├── requirements.txt         # Dependências
├── example.py               # Script de exemplo para testar o pacote
```

## Instalação

Para instalar o pacote, você pode usar o `pip`:

```bash
pip install img_processing
```

Veja o exemplo completo em `example.py`. Basicamente o código abaixo mostra como usar as funcionalidades do pacote:

```python
from img_processing.processing.combination import ImageCombiner
from img_processing.processing.transformation import ImageTransformer
from img_processing.utils.plot import show_image, save_image

# Combinar imagens
combiner = ImageCombiner("img1.jpg", "img2.jpg")
combined = combiner.combine_side_by_side()
save_image(combined, "output/combined.jpg")

# Rotacionar imagem
transformer = ImageTransformer("img1.jpg")
rotated = transformer.rotate(90)
save_image(rotated, "output/rotated.jpg")
```

