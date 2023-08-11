# setup.py
from setuptools import setup, find_packages

setup(
    name="reasoning_workbench",
    version="0.1.0",
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        "console_scripts": [
            "reasoning_workbench=reasoning_workbench.main:main",
        ],
    },
    install_requires=[
        "transformers",
        "bert-score",
        "pandas",
        "matplotlib",
        "tqdm",
        "click",
    ],
)

