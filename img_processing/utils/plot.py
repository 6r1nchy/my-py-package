from PIL import Image
import matplotlib.pyplot as plt
import os

def show_image(image: Image.Image, title: str = "Imagem"):
    """Exibe a imagem usando matplotlib."""
    plt.imshow(image, cmap='gray' if image.mode == 'L' else None)
    plt.title(title)
    plt.axis('off')
    plt.show()

def save_image(image: Image.Image, path: str):
    """Salva a imagem no caminho especificado."""
    directory = os.path.dirname(path)
    if directory and not os.path.exists(directory):
        os.makedirs(directory)
    image.save(path)
