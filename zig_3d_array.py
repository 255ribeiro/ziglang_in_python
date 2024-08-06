# test.py 
import numpy as np 
from numpy.ctypeslib import ndpointer 
import ctypes

from pathlib import Path


lib_folder = Path() / 'zig-out' /'bin'

libfile = lib_folder / "bib_array.dll"

zig_dll = ctypes.cdll.LoadLibrary(libfile.absolute())


array_to_c = ndpointer(dtype=np.uintp, ndim=1, flags='C')  



_foobar = zig_dll.test_3darr_func
_foobar.argtypes = [ array_to_c , array_to_c , ctypes.c_size_t, ctypes.c_size_t, ctypes.c_size_t ] 
_foobar.restype = None 

def process_3d_array(x):
    dim1, dim2, dim3 = x.shape
    y = np.zeros_like(x)
    # Convert to 1D representation for ctypes
    xpp = (x.__array_interface__['data'][0] + np.arange(dim1 * dim2 * dim3) * x.itemsize).astype(np.uintp)
    ypp = (y.__array_interface__['data'][0] + np.arange(dim1 * dim2 * dim3) * y.itemsize).astype(np.uintp)
    # Call the C function
    #_foobar(xpp, ypp, dim1, dim2, dim3)
    return y, xpp, ypp

if __name__ == '__main__': 
    x = np.arange(27.).reshape((3, 3, 3)) 
    y, xpp, ypp = process_3d_array(x)
    print(x)
    print("out")
    print(y)
    print(xpp.shape)


  
    