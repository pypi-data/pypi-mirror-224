from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 11',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='FastSetup',
  version='0.0.1',
  description='Static code in python scripts',
  url='',  
  author='Tareq Abeda',
  author_email='TareqAbeda@outlook.com',
  license='MIT', 
  classifiers=classifiers,
  keywords='FastSetup', 
  packages=find_packages(),
  install_requires=['pandas', 'datetime', 'Logging'] 
)
