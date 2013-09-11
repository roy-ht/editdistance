try:
    from setuptools import setup, Extension
except:
    from distutils import setup, Extension

ext_modules = [Extension('editdistance._editdistance', ['editdistance/_editdistance.cpp'], language='c++')]

setup(name="levenshtein",
      version='0.1',
      description="Yet another implementation of the edit distance(Levenshtein distance) by Cython powered with fast algorithm",
      long_description='',
      author='Hiroyuki Tanaka',
      author_email='aflc0x@gmail.com',
      url='https://www.github.com/aflc/levenshtein',
      ext_modules=ext_modules,
      packages=['editdistance'],
      classifiers=[
      'License :: OSI Approved :: MIT License',
      'Programming Language :: Python',
      ]
      )
