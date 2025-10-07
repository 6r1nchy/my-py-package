from PIL import Image
import os

class ImageCombiner:
    def __init__(self, path_img1: str, path_img2: str):
        self.path_img1 = path_img1
        self.path_img2 = path_img2
        self.image1 = None
        self.image2 = None
        self.combined = None

    def load_images(self):
        """Carrega as duas imagens a partir dos caminhos fornecidos."""
        if not os.path.exists(self.path_img1) or not os.path.exists(self.path_img2):
            raise FileNotFoundError("Uma ou ambas as imagens não foram encontradas.")
        
        self.image1 = Image.open(self.path_img1)
        self.image2 = Image.open(self.path_img2)

    def combine_side_by_side(self):
        """Combina as imagens lado a lado."""
        if self.image1 is None or self.image2 is None:
            self.load_images()

        # Redimensiona para mesma altura
        h1 = self.image1.height
        h2 = self.image2.height
        target_height = min(h1, h2)

        img1_resized = self.image1.resize((int(self.image1.width * target_height / h1), target_height))
        img2_resized = self.image2.resize((int(self.image2.width * target_height / h2), target_height))

        total_width = img1_resized.width + img2_resized.width
        self.combined = Image.new('RGB', (total_width, target_height))
        self.combined.paste(img1_resized, (0, 0))
        self.combined.paste(img2_resized, (img1_resized.width, 0))

        return self.combined

    def save_combined(self, output_path: str):
        """Salva a imagem combinada no caminho especificado."""
        if self.combined is None:
            raise ValueError("Nenhuma imagem combinada foi gerada ainda.")
        self.combined.save(output_path)
