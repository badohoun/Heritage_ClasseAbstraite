from setuptools import setup , find_packages

setup(
    name='packaging',
    version='0.0.0',
    packages=find_packages(),
    #specify the package metadata
    author='Espoir BADOHOUN',
    author_email = 'your_email@example.com',
    description='A simple package for packaging',
    license='MIT',
    install_requires=[
        "numpy==1.24.3"
    ],
    setup_requires=[
        "wheel"
    ]
)