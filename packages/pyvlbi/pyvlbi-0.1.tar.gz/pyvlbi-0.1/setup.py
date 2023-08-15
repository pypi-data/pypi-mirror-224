from setuptools import setup, find_packages


setup(
  name         = 'pyvlbi',
  version      = '0.1',
  license      = 'MIT',  # https://help.github.com/articles/licensing-a-repository
  description  = 'Package for VLBI simulation', 
  author       = 'Xiaolong Yang',
  author_email = 'yxl@pku.edu.cn',
  url          = 'https://github.com/yxl-dev/pyvlbi',   # github or website
  download_url = 'https://github.com/yxl-dev/pyvlbi',
  keywords     = ['VLBI', 'Radio'], 
  packages     = ['pyvlbi', 'pyvlbi.ant', 'pyvlbi.models', 'pyvlbi.sat'],
  package_data = {'': ['*.so','*.ant','*.jpg','*.obj','*.sat','*.dat','*.bsp']},
  install_requires = ['numpy','astropy','poliastro','skyfield','mayavi','viscid','trimesh','pillow','extension_helpers'],
  include_package_data	=	True,
  classifiers  = ['Development Status :: 3 - Alpha', 
  # 3 - Alpha,
  # 4 - Beta,
  # 5 - Production/Stable
  'Intended Audience :: Developers',
  'Topic :: Software Development :: Build Tools',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3',
  'Programming Language :: Python :: 3.4',
  'Programming Language :: Python :: 3.5',
  'Programming Language :: Python :: 3.6',
  ],
)