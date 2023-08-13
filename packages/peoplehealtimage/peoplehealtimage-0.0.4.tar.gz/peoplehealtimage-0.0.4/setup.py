from setuptools import setup, find_packages

VERSION = '0.0.4'
DESCRIPTION = 'Detecção de faces em imagens'
LONG_DESCRIPTION = 'Este pacote é capaz de detectar faces em imagens.'

# Setting up
setup(
    name="peoplehealtimage",
    version=VERSION,
    author="Luis Eduardo",
    author_email="duardos36@gmail.com",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    #long_description_content_type='text/markdown',
    packages= ['peoplehealtimage'],
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
