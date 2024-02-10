from Cython.Build import cythonize

def pdm_build_update_setup_kwargs(context, kwargs):
    kwargs.update(ext_modules=cythonize("src/editdistance/bycython.pyx"))
