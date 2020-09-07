import zarrita
import numpy as np
from numcodecs import GZip

h = zarrita.get_hierarchy('test.zr3')
a = h['arthur/dent']
a_ref = np.zeros((4, 4))
a_ref[2, 1] = 3

assert a.shape == (4, 4)
assert a.dtype == np.dtype('float64')
assert a.chunk_shape == (2, 2)
assert a.compressor == GZip(level=1)
assert a.attrs == {'answer': 42, 'question': 'life'}
assert np.all(a[:, :] == a_ref)
