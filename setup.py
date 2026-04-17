import warnings

from setuptools import setup, find_packages

# Suppress all warnings
warnings.filterwarnings("ignore")

setup(
    name='sentinel-authenticator',
    version='0.0.1',
    packages=find_packages()
)
