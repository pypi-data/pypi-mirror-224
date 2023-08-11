from setuptools import setup, find_packages


setup(
  name='writersimple',
  version='1.4.0',
  author='korbolajnennikolaj',
  author_email='korbolajnennikolaj@gmail.com',
  description='writer help write',
  long_description="writer can write revers, combo, and more",
  packages=find_packages(),
  install_requires=['requests>=2.25.1'],
  classifiers=[
    'Programming Language :: Python :: 3.11',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent'
  ],
  python_requires='>=3.7'
)
