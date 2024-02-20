"""setuptools file for the package."""
import os

from setuptools import find_packages
from setuptools import setup

PACKAGE_NAME = "py_apt_mirror"

EXTRAS = {
    'dev-tools': ['flake8',
                  'flake8-bugbear',
                  'flake8-builtins',
                  'flake8-comprehensions',
                  'flake8-docstrings',
                  'flake8-eradicate',
                  'flake8-expression-complexity',
                  'flake8-import-order',
                  'flake8-import-single',
                  'flake8-print',
                  'flake8-return',
                  'pep8-naming']
}

with open("VERSION", "r") as versionFile:
    version = versionFile.read().strip()

with open(os.path.join(PACKAGE_NAME, "__version__.py"), "w") as versionFile:
    versionFile.write('"""Auto-generated version file."""\n')
    versionFile.write('VERSION = "{}"'.format(version))

setup(
    name=PACKAGE_NAME,
    version=version,
    description='A mirror for apt repositories',
    url='https://github.com/TheFrisbeeNinja/py-apt-mirror',
    author='Kenji Ryan Yamamoto',
    author_email='TheFrisbeeNinja@github',
    license="GPLv3",
    py_modules=find_packages(),
    entry_points={
        'console_scripts': [
            'py-apt-mirror=py_apt_mirror.main:main'
        ]
    },
    extras_require=EXTRAS
)
