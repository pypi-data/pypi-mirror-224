from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = 'Meu primeiro pacote em Python'
LONG_DESCRIPTION = 'Meu primeiro projeto em Python com uma descrição um pouco mais longa'

setup(
        name = "melissa-teste",
        version = VERSION,
        author = "Melissa",
        author_email = "msnmelissaoa15@hotmail.com",
        description = DESCRIPTION,
        long_description = LONG_DESCRIPTION,
        packages = find_packages(),
        install_requires = [],

        classifiers = [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Education",
            "Programming Language :: Python :: 3",
            "Operating System :: OS Independent"
        ]
)