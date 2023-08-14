from setuptools import setup, find_packages

classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Science/Research',
    'Operating System :: Microsoft :: Windows :: Windows 11',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.11'
]
setup(name = 'spici',
      version = '0.1.0',
      description = 'spice your data',
      long_description = open('README.txt').read()+'\n\n'+open('CHANGELOG.txt').read(),
      long_description_content_type = 'text/markdown',
      url = '',
      author = 'Eklavya Gupta',
      author_email = 'emessage.eg@gmail.com',
      license = 'MIT',
      classifiers = classifiers,
      keywords = 'data prepration',
      pacakages = find_packages(),
      install_requires = ['pandas', 'numpy', 'seaborn', 'matplotlib'],
      )