import numpy as np

from doelab.doe.orthogonal_array import OrthogonalArray as oa


def test_L4_orthogonal_array(test_L4):
    # Test by L4
    array_obj = oa('L4')
    array = array_obj.create_orthogonal_array()
    assert array.shape[0] == 4
    assert array.shape[1] == 3
    assert np.allclose(array, test_L4)

def test_L8_orthogonal_array(test_L8):
    # Test by L8
    array_obj = oa('L8')
    array = array_obj.create_orthogonal_array()
    assert array.shape[0] == 8
    assert array.shape[1] == 7
    assert np.allclose(array, test_L8)

def test_L9_orthogonal_array(test_L9):
    # Test by L9
    array_obj = oa('L9')
    array = array_obj.create_orthogonal_array()
    assert array.shape[0] == 9
    assert array.shape[1] == 4
    assert np.allclose(array, test_L9)
