import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    # name="google-finance-scraper",
    name="gogi-ardihikaru",
    version="0.0.1",
    license='MIT',
    author="Muhammad Febrian Ardiansyah",
    author_email="mfardiansyah@outlook.com",
    description="Modules to extract information from Google Finance",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.8"
)
