from setuptools import setup, Extension
import os, sysconfig

platform = sysconfig.get_platform().lower()
cc = (os.environ.get("CC", "") + os.environ.get("CXX", "")).lower()
is_mingw = ("mingw" in platform) or any(k in cc for k in ["mingw", "gcc"])

extra_compile_args = ["-O3", "-std=c++17"] if is_mingw else ["/O2", "/std:c++17", "/EHsc"]

ext = Extension(
    name="_dna_hmm",  # <<< IMPORTANTÍSIMO: con guion bajo
    sources=[
        "cpp/dna_hmm.cpp",
        "cpp/dna_hmm_wrap.cxx",  # generado por SWIG
    ],
    include_dirs=["cpp"],
    language="c++",
    extra_compile_args=extra_compile_args,
)

setup(
    name="dna_hmm",
    version="0.1.0",
    description="HMM DNA (SWIG + C++)",
    ext_modules=[ext],
)
