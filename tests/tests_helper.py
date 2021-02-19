import unittest

import numpy as np
from niftiprocessing import numpyhelper


class TestNumpyHelper(unittest.TestCase):

    def test_normalize_1_1(self):
        test_input = [1., 2., 3., 4., 5.]
        expected_output = np.array([0., 0.25, 0.5, 0.75, 1.])
        test_output = numpyhelper.normalize(test_input)

        self.numpy_array_assertions_1(expected_output, test_output)

    def test_normalize_1_2(self):
        test_input = [5., 4., 3., 2., 1.]
        expected_output = np.array([1., 0.75, 0.5, 0.25, 0.])
        test_output = numpyhelper.normalize(test_input)

        self.numpy_array_assertions_1(expected_output, test_output)

    def numpy_array_assertions_1(self, expected_output, test_output):
        # Value(s)
        self.assertTrue((expected_output == test_output).all(), f"{expected_output} != {test_output}")
        # Object type(s)
        self.assertEqual(type(expected_output), type(test_output), f"{type(expected_output)} != {type(test_output)}")
        # Value type(s)
        self.assertEqual(expected_output.dtype, test_output.dtype, f"{expected_output.dtype} != {test_output.dtype}")


if __name__ == '__main__':
    unittest.main()