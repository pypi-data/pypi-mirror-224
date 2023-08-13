from setuptools import setup

VERSION = '0.0.6'
DESCRIPTION = 'Detecção de faces em imagens'
LONG_DESCRIPTION = 'Este pacote é capaz de detectar faces em imagens.'

# Carregando o conteúdo do arquivo README
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# Setting up
setup(
    name="peoplefaceimage",
    version=VERSION,
    author1="Victor Macedo",
    author_email1="victmacc@ufpi.edu.br",
    author2="Luis Eduardo",
    author_email2="duardos26@gmail.com",
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=['peoplefaceimage'],
    install_requires=[
        'opencv-python',
        'os'
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
)
