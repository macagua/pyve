""" package installer """

from setuptools import setup

long_description = (
    open('README.rst').read()
    + '\n' +
    'License\n'
    '*******\n'
    + '\n' +
    open('LICENSE').read()
    + '\n' +
    'Contributors\n'
    '************\n'
    + '\n' +
    open('docs/CONTRIBUTORS.rst').read()
    + '\n')

setup(
    name="pyve",
    version="0.1",
    description="Documentation from Python Venezuela Community",
    long_description=long_description,
    # Get more https://pypi.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries",
        "License :: OSI Approved :: GNU General Public License",
        "Programming Language :: Python",
        "Programming Language :: Python :: Python 3",
        "Operating System :: OS Independent",
    ],
    keywords="python venezuela pyve community package example",
    author="Leonardo J. Caballero G.",
    author_email="leonardocaballero@gmail.com",
    url="https://twitter/macagua",
    download_url="https://github.com/macagua/pyve",
    license="GPL",
    platforms="Unix",
    packages=["pyve/"],
    include_package_data=True,
    install_requires=[
        'setuptools',
    ],
)

