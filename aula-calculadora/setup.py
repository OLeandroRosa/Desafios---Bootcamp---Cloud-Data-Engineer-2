from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.1'
DESCRIPTION = 'Calculadora Soma, Subtração, Multiplicação e Divisão'
LONG_DESCRIPTION = 'o pacote é para testar como faz o upload de pacotes em python e contem um programa de Calculadora simples'

# Setting up
setup(
    name="calculadora",
    version=VERSION,
    author="Leandro Rosa",
    author_email="<leandro.rdeoliveira200@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=[''],
    keywords=['python', 'calculadora'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
