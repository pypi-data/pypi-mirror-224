from setuptools import setup, find_packages

setup(
    name="atolibrary",
    version="0.0.2",
    packages=find_packages(),
    install_requires=[
        'Pillow>=9.0.0',
        'requests'
    ],
)
