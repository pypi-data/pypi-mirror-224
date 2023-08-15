import pathlib
from setuptools import setup, find_packages

HERE = pathlib.Path(__file__).parent

#README = (HERE / "README.md").read_text()

setup(
    name="cap-tsf-lib1-beta",
    version="1.0.0",
    description="Custom keywords",
    #long_description=README,
    #long_description_content_type="text/markdown",
    author="Pallav Kumar",
    author_email="pallav05.star@gmail.com",
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
    packages=find_packages(),
    install_requires=[]
)