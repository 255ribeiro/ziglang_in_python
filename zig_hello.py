import ctypes 
from pathlib import Path

lib_folder = Path() / 'zig-out' /'bin'

libfile = lib_folder / "bib_hello.dll"

hw = ctypes.cdll.LoadLibrary(libfile.absolute())
hello = hw.test_func


hello()