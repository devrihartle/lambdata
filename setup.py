import setuptools

REQUIRED=['numpy','pandas']

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="devrihartle", # Replace with your own username
    version="0.0.1",
    author="devrihartle",
    author_email="devrihartle@gmail.com",
    description="a collection of helper functions",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/devrihartle/lambdata",
    project_urls={
        "Bug Tracker": "https://github.com/pypa/sampleproject/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    install_requires=REQUIRED,
    python_requires=">=3.6",
)