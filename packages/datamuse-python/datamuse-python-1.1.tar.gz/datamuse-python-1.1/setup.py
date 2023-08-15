from setuptools import setup, find_packages

setup(
    name="datamuse-python",
    version="1.1",
    description="A collection of functions using the Datamuse API.",
    author="Animesh Srivastava",
    author_email="animeshsrivastava2003@email.com",
    packages=find_packages(),
    install_requires=[
        "requests",
        "beautifulsoup4",
        "json"
    ],
)
