#!/usr/bin/env python
from __future__ import division, print_function

def configuration(parent_package='',top_path=None):
    global config
    from numpy.distutils.misc_util import Configuration
    # from numpy.distutils.fcompiler import get_default_fcompiler, CompilerNotFound
    from numpy.distutils.fcompiler import CompilerNotFound

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
    config = Configuration('minimalf2py',
                           parent_name=parent_package,
                           top_path=top_path)
    config.add_subpackage('tests')
    config.add_extension(name='add',
                         sources=['add.f', 'add.pyf'],
                         extra_f90_compile_args=f90flags,)
    return config

def get_default_fcompiler(osname=None, platform=None, requiref90=False,
                          c_compiler=None):
    """Determine the default Fortran compiler to use for the given
    platform.
    This version is copied from numpy.distutils.fcompiler.__init__.py
    but with a hack to prioritize flang"""
    from numpy.distutils.fcompiler import available_fcompilers_for_platform, _find_existing_fcompiler
    from numpy.distutils import log

    matching_compiler_types = available_fcompilers_for_platform(osname,
                                                                platform)
    # Move flang to front of list so it has top priority
    if 'flang' in matching_compiler_types:
        matching_compiler_types.insert(0, 'flang')
    log.info("get_default_fcompiler: matching types: '%s'",
             matching_compiler_types)
    compiler_type =  _find_existing_fcompiler(matching_compiler_types,
                                              osname=osname,
                                              platform=platform,
                                              requiref90=requiref90,
                                              c_compiler=c_compiler)
    return compiler_type

if __name__ == '__main__':
    print('This is the wrong setup.py file to run')
