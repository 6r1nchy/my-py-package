from setuptools import setup, find_packages

setup(
    name="img_processing",
    version="0.1.0",
    author="QGom3s",
    description="Pacote simples para combinar e transformar imagens com Python",
    packages=find_packages(),
    install_requires=[
        "Pillow>=10.0.0",
        "matplotlib>=3.8.0"
    ],
    python_requires=">=3.8",
)
