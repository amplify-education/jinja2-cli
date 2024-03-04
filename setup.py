#!/usr/bin/env python
"""
jinja2-cli
==========

.. code:: shell

  $ jinja2 helloworld.tmpl data.json --format=json
  $ cat data.json | jinja2 helloworld.tmpl
  $ curl -s http://httpbin.org/ip | jinja2 helloip.tmpl
  $ curl -s http://httpbin.org/ip | jinja2 helloip.tmpl > helloip.html
"""
import os
import re

from setuptools import find_packages, setup

install_requires = ["jinja2"]
tests_requires = ["pytest", "flake8"]

VERSION_REGEX = re.compile(
    r"""
    ^__version__\s=\s
    ['"](?P<version>.*?)['"]
    """,
    re.MULTILINE | re.VERBOSE,
)
VERSION_FILE = os.path.join("jinja2cli", "__init__.py")


def get_version():
    """Reads the version from the package"""
    with open(VERSION_FILE, encoding="utf8") as handle:
        lines = handle.read()
        result = VERSION_REGEX.search(lines)
        if result:
            return result.groupdict()["version"]
        raise ValueError("Unable to determine __version__")


setup(
    name="jinja2-cli",
    version=get_version(),
    author="Matt Robenolt",
    author_email="matt@ydekproductions.com",
    url="https://github.com/mattrobenolt/jinja2-cli",
    description="A CLI interface to Jinja2",
    long_description=__doc__,
    packages=find_packages(exclude=["tests"]),
    zip_safe=False,
    license="BSD",
    install_requires=install_requires,
    extras_require={
        "yaml": install_requires + ["pyyaml"],
        "toml": install_requires + ["toml"],
        "xml": install_requires + ["xmltodict"],
        "tests": install_requires + tests_requires,
        "hjson": install_requires + ["hjson"],
        "json5": install_requires + ["json5"],
    },
    tests_require=tests_requires,
    include_package_data=True,
    entry_points={"console_scripts": ["jinja2 = jinja2cli:main"]},
    classifiers=[
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "Operating System :: OS Independent",
        "Topic :: Software Development",
    ],
)
