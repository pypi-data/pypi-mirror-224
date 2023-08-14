from setuptools import find_packages, setup

setup(
    name="gflownets",
    description="A Python library for training and using Generative Flow Networks (GFlowNets)",
    version="0.0.2",
    license="MIT",
    author="Mike Arpaia",
    author_email="mike@arpaia.co",
    packages=find_packages("src"),
    package_dir={"": "src"},
    url="https://github.com/marpaia/gflownets",
    keywords="machine learning",
    install_requires=[],
)
