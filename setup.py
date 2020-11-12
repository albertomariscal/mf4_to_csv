import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="mf4_to_csv", # Replace with your own username
    version="0.0.1",
    author="Alberto L. Mariscal",
    author_email="-",
    description="Conversor from MF4 to CSV with a DBC File",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/albertomariscal/mf4_to_csv",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.8.3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)