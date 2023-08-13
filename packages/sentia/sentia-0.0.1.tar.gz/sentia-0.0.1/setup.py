import setuptools

with open(".\\readme.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="sentia", 
    version="0.0.1",
    author="Locutusque",
    author_email="locutusque.airshipcraft@gmail.com",
    description="A text generation model combining multiple neural network architectures",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Locutusque/SENTIA.py",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
