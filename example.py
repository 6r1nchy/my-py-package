from img_processing.processing.combination import ImageCombiner
from img_processing.processing.transformation import ImageTransformer
from img_processing.utils.plot import show_image, save_image

# Caminhos das imagens de entrada
img1_path = "images/img1.jpg"
img2_path = "images/img2.jpg"

# Combinação lado a lado
combiner = ImageCombiner(img1_path, img2_path)
combined_image = combiner.combine_side_by_side()
show_image(combined_image, title="Imagem Combinada")
save_image(combined_image, "output/combined.jpg")

# Transformação: rotação da primeira imagem
transformer = ImageTransformer(img1_path)
rotated_image = transformer.rotate(90)
show_image(rotated_image, title="Imagem Rotacionada")
save_image(rotated_image, "output/rotated.jpg")
