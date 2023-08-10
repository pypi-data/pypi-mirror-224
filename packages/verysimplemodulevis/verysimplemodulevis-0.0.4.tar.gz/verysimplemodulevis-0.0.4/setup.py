from setuptools import setup, find_packages

VERSION = '0.0.4'
DESCRIPTION = 'Meu primeiro projeto em Python'
LONG_DESCRIPTION = 'Esta é a descrição longa do meu projeto.'

# Configurando o setup
setup(
    name="verysimplemodulevis",
    version=VERSION,
    author="Victor Macedo",
    author_email="victormacedocarvalho09@gmail.com",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    packages=['verysimplemodulevis'],  # Adicione "verysimplemodule" à lista de pacotes
    install_requires=[],
)