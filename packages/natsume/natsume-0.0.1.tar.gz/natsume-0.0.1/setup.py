from setuptools import Extension, find_packages, setup

setup(
    name="natsume",
    version="0.0.1",
    description="A Japanese text frontend toolkit",
    author="Rui Hu",
    author_email="franciskomizu@gmail.com",
    url="https://github.com/Francis-Komizu/natsume",
    license="GNU Licence",
    packages=find_packages(),
    platforms="any",
    install_requires=[
        "numpy >= 1.20.0",
    ]
)