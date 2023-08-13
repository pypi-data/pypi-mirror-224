from setuptools import setup

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="alto-ds",
    version="v1.2023.8.0",
    description="A package for the Alto Data Science team.",
    packages=["alto_ds"],  # [your_package_name]
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    author="Andaman Lekawat",
    author_email="andaman.l@altotech.ai",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent",
    ],
    install_requires=["crate >= 0.33.0"],
    extras_require={
        "dev": ["pytest>=7.0", "twine>=4.0.2"],
    },
    python_requires=">=3.10",
)