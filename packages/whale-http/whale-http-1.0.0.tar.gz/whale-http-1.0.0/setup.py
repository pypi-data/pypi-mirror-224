import os

from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))


def long_description():
    with open("README.md", encoding="utf-8") as f:
        return f.read()


def read_requirements(filename):
    try:
        with open(filename, encoding="utf-8") as f:
            return [line.rstrip() for line in f]
    except OSError as e:
        raise OSError(os.getcwd()) from e


setup(
    name="whale-http",
    version="1.0.0",
    url="https://github.com/yuexl/whale-http",
    description="Fork from http-prompt(2.1.0), add ability of project manage.",
    long_description=long_description(),
    long_description_content_type="text/markdown",
    author="dajing",
    author_email="yueblagon@gmail.com",
    license="MIT",
    packages=["http_prompt", "http_prompt.context"],
    entry_points="""
        [console_scripts]
        whale-http=http_prompt.cli:cli
    """,
    install_requires=read_requirements("requirements.txt"),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: MIT License",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Software Development",
        "Topic :: System :: Networking",
        "Topic :: Terminals",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.8",
    ],
)
