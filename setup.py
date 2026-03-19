from setuptools import setup, find_packages

setup(
    name="deepseek-cli",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "typer>=0.9.0",
        "rich>=13.0.0",
        "openai>=1.10.0",
        "python-dotenv>=1.0.0",
        "prompt_toolkit>=3.0.0"
    ],
    entry_points={
        "console_scripts": [
            "deepseek=deepseek_cli.main:run",
        ],
    },
)
