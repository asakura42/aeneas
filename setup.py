from setuptools import Extension, setup
from numpy import get_include

# prepare Extension objects
EXTENSION_CDTW = Extension(
    name="aeneas.cdtw.cdtw",
    sources=[
        "aeneas/cdtw/cdtw_py.c",
        "aeneas/cdtw/cdtw_func.c",
        "aeneas/cint/cint.c"
    ],
    include_dirs=[
        get_include()
    ]
)
EXTENSION_CMFCC = Extension(
    name="aeneas.cmfcc.cmfcc",
    sources=[
        "aeneas/cmfcc/cmfcc_py.c",
        "aeneas/cmfcc/cmfcc_func.c",
        "aeneas/cwave/cwave_func.c",
        "aeneas/cint/cint.c"
    ],
    include_dirs=[
        get_include()
    ]
)
EXTENSION_CEW = Extension(
    name="aeneas.cew.cew",
    sources=[
        "aeneas/cew/cew_py.c",
        "aeneas/cew/cew_func.c"
    ],
    libraries=[
        "espeak"
    ]
)
EXTENSION_CFW = Extension(
    name="aeneas.cfw.cfw",
    sources=[
        "aeneas/cfw/cfw_py.cc",
        "aeneas/cfw/cfw_func.cc"
    ],
    include_dirs=[
        "aeneas/cfw/festival",
        "aeneas/cfw/speech_tools"
    ],
    libraries=[
        "Festival",
        "estools",
        "estbase",
        "eststring",
    ]
)

setup(
    ext_modules=[
        EXTENSION_CEW,
        EXTENSION_CDTW,
        EXTENSION_CMFCC,
        EXTENSION_CFW
    ]
)
