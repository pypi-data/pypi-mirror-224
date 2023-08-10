from __future__ import absolute_import, unicode_literals


# start delvewheel patch
def _delvewheel_patch_1_5_0():
    import os
    libs_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, 'filepattern.libs'))
    if os.path.isdir(libs_dir):
        os.add_dll_directory(libs_dir)


_delvewheel_patch_1_5_0()
del _delvewheel_patch_1_5_0
# end delvewheel patch

from .filepattern import FilePattern

from .functions import infer_pattern, get_regex

__all__ = ["FilePattern"]
from . import _version
__version__ = _version.get_versions()['version']
