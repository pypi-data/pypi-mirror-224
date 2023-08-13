import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="acquabr",
    version="0.1.0",
    author="Leonardo Maciel de Sousa",
    author_email="leonardo.maciel3@academico.ufpb.br",
    description="Uma biblioteca para análise de dados hidrológicos e geoespaciais relacionados ao Brasil.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "tqdm",
        "requests",
        "pandas",
        "geopandas",
        "pyproj",
        "utm",
        "srtm",
        "numpy",
    ],
    extras_require={
        "dev": [
            "pytest",
            "coverage",
        ],
    },
    python_requires=">=3.6",
)
