from setuptools import find_packages, setup

setup(
    name="mcqgenerator",
    version="0.0.1",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "streamlit",
        "python-dotenv",
        "pypdf",
        "transformers",
        "accelerate",
        "torch",
        "huggingface_hub",
        "langchain",
    ],
)