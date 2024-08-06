# test.py 
import numpy as np 
from numpy.ctypeslib import ndpointer 
import ctypes

from pathlib import Path


lib_folder = Path() / 'zig-out' /'bin'

libfile = lib_folder / "bib_array.dll"

zig_dll = ctypes.cdll.LoadLibrary(libfile.absolute())


array_2d_to_c = ndpointer(dtype=np.uintp, ndim=1, flags='C') 



_foobar = zig_dll.test_2darr_func
_foobar.argtypes = [ array_2d_to_c , array_2d_to_c , ctypes.c_size_t, ctypes.c_size_t] 
_foobar.restype = None 

def foobar(x):
    dim1, dim2 = x.shape
    y = np.zeros_like(x) 
    xpp = (x.__array_interface__['data'][0] + np.arange(x.shape[0] ) * x.strides[0]).astype(np.uintp)
    ypp = (y.__array_interface__['data'][0] + np.arange(y.shape[0] ) * y.strides[0]).astype(np.uintp)
 
    m = ctypes.c_size_t(x.shape[0]) 
    n = ctypes.c_size_t(x.shape[1]) 
    _foobar(xpp, ypp, m, n) 
    return y , xpp

if __name__ == '__main__': 
    x = np.arange(6.).reshape((2, 3)) 
    y, xpp = foobar(x)
    print(x)
    print("out")
    print(y)
    print(x.__array_interface__['data'][0] + np.arange( x.shape[0] ) * x.strides[0])


    