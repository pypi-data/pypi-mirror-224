from setuptools import setup, find_packages

VERSION = '0.0.2'
DESCRIPTION = 'Meu primeiro pacote em python'
LONG_DESCRIPTION = 'Descricao detalhada do meu pacote.'

# Setting up
setup(
    name="multiplicarea",
    version=VERSION,
    author="Luis Eduardo",
    author_email="le1307114@gmail.com",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    packages=find_packages(),
    install_requires=[],
    keywords='python pacote example',
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
