from setuptools import setup, find_packages

setup(
    name="pythonscriptoperations",
    version="0.1.1",
    packages=find_packages(),
    install_requires=[
        # 'none'
    ],
    author="Stijn Raeymaekers",
    description="A package to manage and execute Python operations.",
    license="MIT",
    keywords="python script operations manager console selection",
    url="https://github.com/NotCoffee418/PythonScriptOperations",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ]
)
