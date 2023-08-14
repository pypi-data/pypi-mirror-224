from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.1'
DESCRIPTION = 'Quantum and classical problem solvers'
LONG_DESCRIPTION = 'A package that allows to build and solve quantum and classical problems using predefined solvers and problems.'

# Setting up
setup(
    name="QHyper",
    version=VERSION,
    author="ACK Cyfronet AGH",
    author_email="tomasz.lamza@cyfronet.pl",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['numpy', 'PennyLane', 'tdqm', 'sympy', 'dwave-system', 'gurobipy', 'pandas', 'wfcommons'],
    keywords=['python', 'qhyper', 'quantum', 'solver', 'experiment'],
    license='MIT',
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
