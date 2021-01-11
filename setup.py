from distutils.core import setup
setup(
  name = 'webscrape',
  author_email = 'example@example.com',
  version = '0.0.1',
  classifiers = [
      "Programming Language :: Python :: 3",
  ],
  description = ' webscrape',
  licence = 'MIT',
  instal_requires =['requests','bs4'],
  packages = ['webscrape'],
  author = 'ninjamar',
  python_require = '>=3.7',
  url = 'https://github.com/ninjamar/webscrape'
)
