from setuptools import setup, find_packages

setup(
    name="mockfly-python-sdk",
    version="0.0.1",
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
    author="Mockfly",
    author_email="mockflydev@gmail.com",
    url="https://github.com/Mockfly-Dev/mockfly-python-sdk.git",
    description="Mockfly SDK for Python",
    long_description=open('README.md').read(), 
    long_description_content_type="text/markdown",
)
