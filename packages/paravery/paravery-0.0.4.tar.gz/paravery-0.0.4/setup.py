from setuptools import setup, find_packages

VERSION = '0.0.4'
DESCRIPTION = 'Meu primeiro pacote em python'
LONG_DESCRIPTION = 'Descricao detalhada do meu pacote.'

# Setting up
setup(
    name="paravery",
    version=VERSION,
    author="Luis Eduardo",
    author_email="duardos36@gmail.com",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    packages=['paravery'],
    install_requires=[],
)
