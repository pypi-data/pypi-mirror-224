from setuptools import setup, Extension, find_packages

tempdata = Extension(
    'tempdata',
    sources = [
        'src/tempdata_module.c',
        'src/tempdata.c'
    ],
    include_dirs = [
        'include',
    ],
)

setup(
    name            = 'tempdata',
    version         = '1.0',
    packages        = find_packages(),
    description     = 'Python package of manage temporary data based on types.',
    ext_modules     =   [tempdata],
)
