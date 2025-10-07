from PIL import Image
import os

class ImageTransformer:
    def __init__(self, image_path: str):
        self.image_path = image_path
        self.image = None

    def load_image(self):
        """Carrega a imagem a partir do caminho fornecido."""
        if not os.path.exists(self.image_path):
            raise FileNotFoundError("Imagem não encontrada.")
        self.image = Image.open(self.image_path)

    def rotate(self, degrees: int):
        """Rotaciona a imagem em graus."""
        if self.image is None:
            self.load_image()
        return self.image.rotate(degrees, expand=True)

    def resize(self, width: int, height: int):
        """Redimensiona a imagem para largura e altura especificadas."""
        if self.image is None:
            self.load_image()
        return self.image.resize((width, height))

    def flip_horizontal(self):
        """Espelha a imagem horizontalmente."""
        if self.image is None:
            self.load_image()
        return self.image.transpose(Image.FLIP_LEFT_RIGHT)

    def flip_vertical(self):
        """Espelha a imagem verticalmente."""
        if self.image is None:
            self.load_image()
        return self.image.transpose(Image.FLIP_TOP_BOTTOM)
