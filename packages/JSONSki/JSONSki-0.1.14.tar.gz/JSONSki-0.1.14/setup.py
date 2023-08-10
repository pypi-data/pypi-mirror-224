# import os
# import platform
# import subprocess
# from setuptools import setup, Extension
# from setuptools.command.build_ext import build_ext
# import sys
# import setuptools

# # Extension module
# # JSONSKi_module = Extension(
# #     'JSONSki',
# #     sources=['./example1.cpp'],
# #     include_dirs=['./example_python/pybind11-master/include','./src','../src', '../src/..','/src','src','example_python','./example_python/QueryAutomaton.h'],
# #      extra_compile_args=['-mavx', '-mavx2', '-mpclmul','-std=c++11']  
# # )

# # JSONSKi_module = Extension(
# #     'JSONSki',
# #     sources=['example1.cpp'],
# #     include_dirs=['../example_python/pybind11-master/include','../src', '../src/..'],
# #      extra_compile_args=['-mavx', '-mavx2', '-mpclmul','-std=c++11']  
# # )

# class CMakeExtension(Extension):
#     def __init__(self, name, sourcedir=''):
#         Extension.__init__(self, name, sources=[])
#         self.sourcedir = os.path.abspath(sourcedir)

# class CMakeBuild(build_ext):
#     def run(self):
#         try:

#             import distutils.spawn

#             # Search for the cmake executable
#             cmake_executable = distutils.spawn.find_executable('cmake')
#             out = subprocess.check_output([cmake_executable, '--version'])
#         except OSError:
#             raise RuntimeError("CMake must be installed to build the following extensions: " +
#                                ", ".join(e.name for e in self.extensions))
#         except subprocess.CalledProcessError as e:
#             print("Error:", e)

#         for ext in self.extensions:
#             self.build_extension(ext)

#     def build_extension(self, ext):
#         extdir = os.path.abspath(os.path.dirname(self.get_ext_fullpath(ext.name)))
#         cmake_args = ['-DCMAKE_LIBRARY_OUTPUT_DIRECTORY=' + extdir,
#                       '-DPYTHON_EXECUTABLE=' + sys.executable]

#         cfg = 'Debug' if self.debug else 'Release'
#         build_args = ['--config', cfg]

#         if platform.system() == "Windows":
#             cmake_args += ['-DCMAKE_LIBRARY_OUTPUT_DIRECTORY_{}={}'.format(cfg.upper(), extdir)]
#             if sys.maxsize > 2**32:
#                 cmake_args += ['-A', 'x64']
#             build_args += ['--', '/m']
#         else:
#             cmake_args += ['-DCMAKE_BUILD_TYPE=' + cfg]
#             build_args += ['--', '-j2']

#         env = os.environ.copy()
#         env['CXXFLAGS'] = '{} -DVERSION_INFO=\\"{}\\"'.format(env.get('CXXFLAGS', ''),
#                                                               self.distribution.get_version())
#         if not os.path.exists(self.build_temp):
#             os.makedirs(self.build_temp)
#         subprocess.check_call(['cmake', ext.sourcedir] + cmake_args, cwd=self.build_temp)
#         subprocess.check_call(['cmake', '--build', '.'] + build_args, cwd=self.build_temp)



import os
import sys
import subprocess
from setuptools import setup, Extension
from setuptools.command.build_ext import build_ext

class CMakeExtension(Extension):
    def __init__(self, name, sourcedir=''):
        Extension.__init__(self, name, sources=[])
        self.sourcedir = os.path.abspath(sourcedir)

class CMakeBuild(build_ext):
    def run(self):
        try:
            out = subprocess.check_output(['cmake', '--version'])
        except OSError:
            raise RuntimeError("CMake must be installed to build the following extensions: " +
                               ", ".join(e.name for e in self.extensions))
        # except subprocess.CalledProcessError as e:
        #      print("Error:", e)

        for ext in self.extensions:
            self.build_extension(ext)

    def build_extension(self, ext):
        extdir = os.path.abspath(os.path.dirname(self.get_ext_fullpath(ext.name)))
        cmake_args = ['-DCMAKE_LIBRARY_OUTPUT_DIRECTORY=' + extdir,
                      '-DPYTHON_EXECUTABLE=' + sys.executable]

        cfg = 'Debug' if self.debug else 'Release'
        build_args = ['--config', cfg]

        if not os.path.exists(self.build_temp):
            os.makedirs(self.build_temp)

        import distutils.spawn
# Search for the cmake executable
        cmake_executable = distutils.spawn.find_executable('cmake')

        os.environ['PATH'] = cmake_executable + os.environ['PATH']

        subprocess.check_call(['cmake', ext.sourcedir] + cmake_args, cwd=self.build_temp)
        subprocess.check_call(['cmake', '--build', '.'] + build_args, cwd=self.build_temp)



AUTHOR = 'AutomataLab'

AUTHOR_EMAILS = 'zhijia@cs.ucr.edu'


with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

# Package information
setup(
    name='JSONSki',
    version='0.1.14',
    author= AUTHOR,
    author_email= AUTHOR_EMAILS,
    description='JSONSki_Python is the Python binding port for JSONSki',
    long_description=long_description,
    long_description_content_type='text/markdown',
    ext_modules=[CMakeExtension("JSONSki")],
    cmdclass=dict(build_ext=CMakeBuild),
    url='https://github.com/your_username/your_repository',
    zip_safe=False,
    python_requires=">=3.6",
        classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Database :: Front-Ends",
        "Topic :: Office/Business :: Financial :: Spreadsheet",
        "Topic :: Scientific/Engineering :: Information Analysis",
        "Topic :: Scientific/Engineering :: Visualization",
        "Topic :: Software Development :: Libraries :: Application Frameworks",
        "Topic :: Software Development :: Widget Sets",
    ]
)