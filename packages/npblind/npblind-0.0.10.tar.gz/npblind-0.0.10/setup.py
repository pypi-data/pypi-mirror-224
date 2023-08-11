import pathlib

from setuptools import find_packages, setup

here = pathlib.Path(__file__).parent.resolve()

# Read long description from the readme.md file
with open("README.md", encoding="utf-8") as f:
    readme = f.read()

with open("LICENSE", encoding="utf-8") as f:
    license_data = f.read()

setup(
    name="npblind",
    version="0.0.10",
    description="A package to help managing data privacy",
    long_description_content_type="text/markdown",
    long_description=readme,
    author="Nopporn Phantawee",
    author_email="n.phantawee@gmail.com",
    url="https://github.com/noppGithub/npgcs",
    license="MIT",
    packages=find_packages(exclude=['tests', '*.tests', '*.tests.*']),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3 :: Only",
    ],
    install_requires=[
        "google-cloud-datacatalog",
        "google-cloud-dlp",
        "npgbq>=2.1.3",
    ],
    extras_require={
        "dev": ["pandas"],
        "test": ["pandas"],
    },
    python_requires=">=3.6, <4",
)
