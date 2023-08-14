import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="acquabr",
    version="0.1.1",
    author="Leonardo Maciel de Sousa",
    author_email="leonardo.maciel3@academico.ufpb.br",
    description="Python Library for Hydrological Analysis in Brazil",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Hydrology",
    ],
    keywords=[
        "hydrology",
        "hydrological analysis",
        "rainfall data Brazil",
        "flow data Brazil",
        "HIDROWEB",
        "rainfall analysis",
        "flow analysis",
        "Brazil rainfall",
        "Brazil flow ",
    ],
    install_requires=[
        "tqdm",
        "requests",
        "pandas",
        "geopandas",
        "pyproj",
        "utm",
        "SRTM.py",
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
