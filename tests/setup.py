# setup.py
from setuptools import find_packages, setup

setup(
    name="erp",
    version="0.1",
    packages=find_packages(),
    install_requires=[  # Adicione suas dependências aqui
        "fastapi",
        "sqlalchemy",
        "pytest",
    ],
    python_requires=">=3.8",
)
