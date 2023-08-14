import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="functionTime",
    version="0.0.1",
    author="Nayan-Chimariya",
    author_email="cnayan789@gmail.com",
    description="decorator to time your function",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Nayan-Chimariya/functionTime",
    packages=setuptools.find_packages(),
    install_requires = ['colorama'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)