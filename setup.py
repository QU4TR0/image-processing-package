from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="Image-Processing",
    version="0.0.1",
    author="Guilherme Pontes",
    author_email="pontesguilhermer@gmail.com",
    description="Pacote de histogramar imagens",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/QU4TR0/image-processing-package",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)