import ctypes 
from pathlib import Path
import numpy as np

lib_folder = Path() / 'zig-out' /'bin'

libfile = lib_folder / "bib_array.dll"

zig_dll = ctypes.cdll.LoadLibrary(libfile.absolute())
array = zig_dll.test_arr_func

arr = np.arange(0,20,1, dtype=np.double).reshape(4,5)
print(array)
print(arr.shape)
array(arr.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
            ctypes.c_size_t(arr.shape[0]),
            ctypes.c_size_t(arr.shape[1])

      )