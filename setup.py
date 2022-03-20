import setuptools
import re
from os import path

def get_version():
    with open("pyamlqt/__init__.py", "r") as f:
        version = re.search(
            r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
            f.read(), re.MULTILINE
        ).group(1)
    return version

readme_path = path.abspath(path.dirname(__file__))
with open(path.join(readme_path, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setuptools.setup(
    name="PyamlQt",
    packages=["pyamlqt"],

    version=get_version(),
    author="Ar-Ray-code",
    author_email="ray255ar@gmail.com",

    url="https://github.com/Ar-Ray-code/PyamlQt",
    description="PyQt6 configuration in yaml format providing the most simple script.",
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords='PyQt yaml',
    license="GPLv3",
    python_requires=">=3.8",
    install_requires=["PyYAML", "PyQt6"],
    classifiers=[
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    project_urls={
        "Source": "https://github.com/Ar-Ray-code/PyamlQt",
        "Tracker": "https://github.com/Ar-Ray-code/PyamlQt/issues",
    },
)