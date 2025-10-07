from PIL import Image
import numpy as np

def image_to_array(image: Image.Image) -> np.ndarray:
    """Converte uma imagem PIL para um array NumPy."""
    return np.array(image)

def array_to_image(array: np.ndarray) -> Image.Image:
    """Converte um array NumPy para uma imagem PIL."""
    return Image.fromarray(array)

def to_grayscale(image: Image.Image) -> Image.Image:
    """Converte uma imagem para escala de cinza."""
    return image.convert("L")

def to_rgb(image: Image.Image) -> Image.Image:
    """Converte uma imagem para RGB."""
    return image.convert("RGB")
