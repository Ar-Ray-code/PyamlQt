import setuptools
import re

def get_version():
    with open("pyamlqt5/__init__.py", "r") as f:
        version = re.search(
            r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
            f.read(), re.MULTILINE
        ).group(1)
    return 

setuptools.setup(
    name="pyyamlqt5",
    version=get_version(),
    author="Ar-Ray-code",
    url="https://github.com/Ar-Ray-code/PyamlQt5",
    python_requires=">=3.8",
    install_requires=["PyYAML", "PyQt5"],
    packages=setuptools.find_packages(),
    project_urls={
        "Source": "https://github.com/Ar-Ray-code/PyamlQt5",
        "Tracker": "https://github.com/Ar-Ray-code/PyamlQt5/issues",
    },
)