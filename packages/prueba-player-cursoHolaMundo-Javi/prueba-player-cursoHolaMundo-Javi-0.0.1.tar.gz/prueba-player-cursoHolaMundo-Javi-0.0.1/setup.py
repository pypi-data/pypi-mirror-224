import setuptools
from pathlib import Path


setuptools.setup(
    name="prueba-player-cursoHolaMundo-Javi",
    version="0.0.1",
    long_description= Path("README.MD").read_text(),
    packages= setuptools.find_packages(
        exclude=["tests"]
    )
)