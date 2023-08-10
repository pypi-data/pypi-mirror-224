from setuptools import setup, find_packages

VERSION = '0.0.3'
DESCRIPTION = 'Meu primeiro pacote em python'
LONG_DESCRIPTION = 'Descricao detalhada do meu pacote.'

# Setting up
setup(
    name="paralelogramoarea",
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
        "Operating System :: OS Independent",
    ],
)
