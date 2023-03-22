# -*- coding: utf-8 -*-
import os
from setuptools import setup

packages = []
root_dir = os.path.dirname(__file__)
if root_dir:
    os.chdir(root_dir)
accepted_filetypes = (".html", ".png", ".svg", ".js", ".css")

for dirpath, dirnames, filenames in os.walk('ab_plugin_notebook'):
    # Ignore dirnames that start with '.'
    if ('__init__.py' in filenames
            or any(x.endswith(accepted_filetypes) for x in filenames)):
        pkg = dirpath.replace(os.path.sep, '.')
        if os.path.altsep:
            pkg = pkg.replace(os.path.altsep, '.')
        packages.append(pkg)

if 'VERSION' in os.environ:
    version = os.environ['VERSION']
else:
    version = os.environ.get('GIT_DESCRIBE_TAG', '0.0.0')

setup(
    name='ab-plugin-notebook',
    version=version,
    packages=packages,
    author='Rémy Le Calloch',
    author_email='remy@lecalloch.net',
    license=open('LICENSE.txt').read(),
    install_requires=[], # dependency management in conda recipe
    url='https://github.com/Pan6ora/ab-plugin-Notebook',
    long_description=open('README.md').read(),
    description='Launch Jupyter Notebook directly in Activity-Browser',
    package_data={'': ['jupyter_config/jupyter_notebook_config.py', 'jupyter_config/custom/custom.js']},
    )
