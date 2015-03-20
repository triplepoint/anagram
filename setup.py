try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'name': 'Anagram',
    'description': 'A library for finding anagrams in a list of words.',
    'author': 'Jonathan Hanson',
    'download_url': 'https://github.com/triplepoint/anagram',
    'author_email': 'jonathan@jonathan-hanson.org',
    'version': '0.1',
    'install_requires': [],
    'packages': [
        'anagram'
    ],
}

setup(**config)
