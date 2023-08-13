from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = 'Detecção de faces em imagens'
LONG_DESCRIPTION = 'Este pacote é capaz de detectar faces em imagens.'

# Setting up
setup(
    name="peoplehealtimage",
    version=VERSION,
    author="peoplehealtimage",
    author_email="duardos36@gmail.com",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    packages=find_packages(),
    install_requires=['OpenCV','OS'],
    keywords='peoplehealtimage',
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
