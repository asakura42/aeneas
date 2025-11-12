import shlex
import subprocess

from numpy import get_include
from setuptools import Extension, setup


def _pkg_config_flags(pkg, flag):
    try:
        out = subprocess.check_output(
            ["pkg-config", flag, pkg], universal_newlines=True
        ).strip()
        return shlex.split(out)
    except Exception:
        return []


ESPEAKNG_CFLAGS = _pkg_config_flags("espeak-ng", "--cflags")
ESPEAKNG_LIBS = _pkg_config_flags("espeak-ng", "--libs")

# prepare Extension objects
EXTENSION_CDTW = Extension(
    name="aeneas.cdtw.cdtw",
    sources=["aeneas/cdtw/cdtw_py.c", "aeneas/cdtw/cdtw_func.c", "aeneas/cint/cint.c"],
    include_dirs=[get_include()],
)
EXTENSION_CMFCC = Extension(
    name="aeneas.cmfcc.cmfcc",
    sources=[
        "aeneas/cmfcc/cmfcc_py.c",
        "aeneas/cmfcc/cmfcc_func.c",
        "aeneas/cwave/cwave_func.c",
        "aeneas/cint/cint.c",
    ],
    include_dirs=[get_include()],
)
EXTENSION_CEW = Extension(
    name="aeneas.cew.cew",
    sources=["aeneas/cew/cew_py.c", "aeneas/cew/cew_func.c"],
    libraries=["espeak-ng"],
    extra_compile_args=ESPEAKNG_CFLAGS,
    extra_link_args=ESPEAKNG_LIBS,
)


setup(ext_modules=[EXTENSION_CEW, EXTENSION_CDTW, EXTENSION_CMFCC])
