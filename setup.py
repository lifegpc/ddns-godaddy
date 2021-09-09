# flake8: noqa
import sys
from ddns_godaddy import __version__
if len(sys.argv) == 2 and sys.argv[1] == "py2exe":
    from distutils.core import setup
    import py2exe
    params = {
        "console": [{
            'script': "ddns_godaddy/__main__.py",
            "dest_base": 'ddns-godaddy',
            'version': __version__,
            'product_name': 'ddns-godaddy',
            'product_version': __version__,
            'company_name': 'lifegpc',
            'description': 'A ddns for godaddy',
        }],
        "options": {
            "py2exe": {
                "optimize": 2,
                "compressed": 1,
                "excludes": ["pydoc"]
            }
        },
        "zipfile": None,
    }
else:
    from setuptools import setup
    params = {
        "install_requires": ["pyyaml", "requests"],
        'entry_points': {
            'console_scripts': ['ddns-godaddy = ddns_godaddy:start']
        }
    }
setup(
    name="ddns-godaddy",
    version=__version__,
    url="https://github.com/lifegpc/ddns-godaddy",
    author="lifegpc",
    author_email="g1710431395@gmail.com",
    classifiers=[
        "License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)",
        "Programming Language :: Python :: 3.7",
    ],
    license="License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)",
    description="A ddns for godaddy",
    long_description="A ddns for godaddy",
    keywords="godaddy;ddns",
    packages=["ddns_godaddy"],
    **params
)
