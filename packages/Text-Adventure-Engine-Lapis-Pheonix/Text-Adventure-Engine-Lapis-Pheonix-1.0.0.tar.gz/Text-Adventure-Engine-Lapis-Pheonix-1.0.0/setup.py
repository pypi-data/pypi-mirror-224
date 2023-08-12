from setuptools import setup, find_packages

setup(
    name="Text-Adventure-Engine-Lapis-Pheonix",
    version="1.0.0",
    author="Lapis Pheonix",
    description="A Text Engine for Text Stories",
    long_description=open("README.md", "r").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/LapisPhoenix/Text-Engine",
    project_urls={
        "Bug Tracker": "https://github.com/LapisPhoenix/Text-Engine/issues"
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    python_requires=">=3.6",
)
