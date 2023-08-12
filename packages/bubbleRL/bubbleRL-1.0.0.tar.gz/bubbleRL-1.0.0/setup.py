import pathlib
from setuptools import find_packages, setup

HERE = pathlib.Path(__file__).parent

VERSION = '1.0.0' 
PACKAGE_NAME = 'bubbleRL'
AUTHOR = 'José Israel Cetina Palomo' 
AUTHOR_EMAIL = 'israel.cetinaa.28@gmail.com'
URL = 'https://github.com/israelcetinaa'

LICENSE = 'MIT'
DESCRIPTION = 'Library for all Bubble.io request methods and utilitys'
LONG_DESCRIPTION = (HERE / "README.md").read_text(encoding='utf-8') 
LONG_DESC_TYPE = "text/markdown"


#Paquetes necesarios para que funcione la libreía. Se instalarán a la vez si no lo tuvieras ya instalado
INSTALL_REQUIRES = [
        'requests',
    ]

setup(
    name=PACKAGE_NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type=LONG_DESC_TYPE,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    url=URL,
    install_requires=INSTALL_REQUIRES,
    license=LICENSE,
    packages=find_packages(),
    include_package_data=True
)