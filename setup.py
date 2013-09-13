try:
    from setuptools import setup, Extension
except:
    from distutils import setup, Extension
# for development
# from Cython.Build import cythonize
# ext_modules = cythonize('editdistance/bycython.pyx')

ext_modules = [Extension('editdistance.bycython', ['editdistance/_editdistance.cpp', 'editdistance/bycython.cpp'])]

setup(name="levenshtein",
      version='0.1',
      description="Fast implementation of the edit distance(Levenshtein distance)",
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
