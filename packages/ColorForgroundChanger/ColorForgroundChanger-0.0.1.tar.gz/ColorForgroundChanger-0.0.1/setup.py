from setuptools import setup, find_packages

classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Education',
    'Operating System :: Microsoft :: Windows :: Windows 11',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3'
]

setup(
  name='ColorForgroundChanger',
  version='0.0.1',
  description='A forground color changer',
  long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url='',  
  author='Dean Brosnan',
  author_email='deangames200@hotmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords='forgroundcolor', 
  packages=find_packages(),
  install_requires=['']
)