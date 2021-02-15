import unittest

import numpy as np
from niftiprocessing import numpyhelper


class TestNumpyHelper(unittest.TestCase):

    def test_normalize_1d(self):
        test_input = [1., 2., 3., 4., 5.]
        expected_output = np.array([0., 0.25, 0.5, 0.75, 1.])

        test_output = numpyhelper.normalize(test_input)

        # Value(s)
        self.assertTrue((expected_output == test_output).all(), f"{expected_output} != {test_output}")
        # Object type(s)
        self.assertEqual(type(expected_output), type(test_output), f"{type(expected_output)} != {type(test_output)}")
        # Value type(s)
        self.assertEqual(expected_output.dtype, test_output.dtype, f"{expected_output.dtype} != {test_output.dtype}")


if __name__ == '__main__':
    unittest.main()