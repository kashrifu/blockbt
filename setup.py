from setuptools import setup, find_packages

setup(
    name="blockbt",
    version="0.1.0-mvp",
    packages=find_packages(),
    install_requires=[
        "click>=8.0",
        "web3>=6.0",
        "polars>=0.20",
        "duckdb>=0.10",
        "sqlparse>=0.4",
        "pyyaml>=6.0",
    ],
    entry_points={
        "console_scripts": ["bbt=bbt.cli:run"],  # Enables bbt run
    },
)

