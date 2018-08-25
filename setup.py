from setuptools import (
    find_packages,
    setup
)


setup(
    name="py-limits",
    version="0.1.0",
    description="command-line util that retrieves rate limits from github",
    url="https://github.com/critical-path/py-limits",
    author="critical-path",
    author_email="n/a",
    license="MIT",
    classifiers=[
        "Development Status :: 2 - Alpha",
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3"
    ],
    keywords="python command-line util rate limits github",
    packages=find_packages(),
    install_requires=[
        "click",
        "requests"
    ],
    extras_require={
        "test": [
            "coveralls",
            "flake8",
            "pytest",
            "pytest-cov",
            "radon",
            "responses"
        ]
    },
    entry_points={
        "console_scripts": [
            "limits=limits.cli:limits"
        ]
    }
)
