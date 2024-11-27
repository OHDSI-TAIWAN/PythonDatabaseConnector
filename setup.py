from setuptools import setup, find_packages

setup(
    name="PythonDatabaseConnector",
    version="0.1.0",
    description="A Python package for connecting to and querying databases.",
    author="Your Name",
    author_email="your_email@example.com",
    license="MIT",
    packages=find_packages(),
    install_requires=[
        "pandas",
        "sqlalchemy",
        "psycopg2-binary",
        "pymssql"
    ],
    python_requires=">=3.6",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
