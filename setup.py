import setuptools
from setuptools import setup

with open("README.md", "r") as f:
    long_description = f.read()
    descr_lines = long_description.split("\n")
    descr_no_gifs = []  # gifs are not supported on PyPI web page
    for dl in descr_lines:
        if not ("<img src=" in dl and "gif" in dl):
            descr_no_gifs.append(dl)

    long_description = "\n".join(descr_no_gifs)


setup(
    # Information
    name="nle-progress",
    description="NetHack Progression Metric",
    long_description=long_description,
    long_description_content_type="text/markdown",
    version="0.1.0",
    url="https://github.com/BartekCupial/nle-progress",
    author="Bartłomiej Cupiał",
    license="MIT",
    keywords="reinforcement learning ai nle nethack",
    project_urls={},
    install_requires=["gym==0.23"],
    extras_require={
        "dev": ["black", "isort>=5.12", "pytest<8.0", "flake8", "pre-commit", "twine"],
    },
    package_dir={"": "./"},
    packages=setuptools.find_packages(where="./", include=["nle_progress*"]),
    package_data={
        "nle_progress": [
            "achievements.json",
        ]
    },
    include_package_data=True,
    python_requires=">=3.8",
)
