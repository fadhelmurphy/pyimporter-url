from setuptools import setup, find_packages

setup(
    name="pygeturl",
    version="0.1.0",
    description="Import Python modules from remote URLs like Go or Bun",
    author="Fadhel Ijlal",
    author_email="fadhelijlalfalah@gmail.com",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "GitPython>=3.1.0",
    ],
    entry_points={
        "console_scripts": [
            "pygeturl=pygeturl.cli:main", 
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
