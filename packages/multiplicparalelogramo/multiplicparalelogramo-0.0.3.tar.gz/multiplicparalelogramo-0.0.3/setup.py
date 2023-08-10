from setuptools import setup, find_packages

VERSION = '0.0.3'
DESCRIPTION = 'Meu primeiro pacote em python'
LONG_DESCRIPTION = 'Descricao detalhada do meu pacote.'

# Setting up
setup(
    name="multiplicparalelogramo",
    version=VERSION,
    author="Luis Eduardo",
    author_email="le1307114@gmail.com",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    packages=find_packages(),
    install_requires=[],
    keywords='python pacote example',
)
