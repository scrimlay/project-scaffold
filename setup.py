from setuptools import setup, find_packages

setup(
    name="project-scaffold",
    version="1.0.0",
    description="A CLI tool to quickly scaffold new development projects with best practices",
    author="scrimlay",
    py_modules=["scaffold"],
    install_requires=[
        # No external dependencies required for basic functionality
    ],
    entry_points={
        "console_scripts": [
            "scaffold=scaffold:main",
        ],
    },
    python_requires=">=3.6",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
)