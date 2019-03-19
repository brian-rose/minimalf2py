#!/usr/bin/env python
from __future__ import division, print_function

def configuration(parent_package='',top_path=None):
    global config
    from numpy.distutils.misc_util import Configuration
    from numpy.distutils.fcompiler import get_default_fcompiler, CompilerNotFound

    compiler = get_default_fcompiler()
    # set some fortran compiler-dependent flags
    f90flags = []
    if compiler == 'gnu95':
        f90flags.append('-fdefault-real-8')
    elif compiler == 'intel' or compiler == 'intelem':
        f90flags.append('-132')
        f90flags.append('-r8')
    #  Set aggressive optimization level
    f90flags.append('-O3')
    #  Suppress all compiler warnings (avoid huge CI log files)
    f90flags.append('-w')
    config = Configuration('minimal_f2py_package',
                           parent_name=parent_package,
                           top_path=top_path)
    config.add_extension(name='add',
                         sources=['add.f', 'add.pyf'],
                         extra_f90_compile_args=f90flags,)
    return config

if __name__ == '__main__':
    print('This is the wrong setup.py file to run')
