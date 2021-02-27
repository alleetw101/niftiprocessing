import niftiprocessing
import sys
import os

# Debugging
if __name__ == '__main__':
    test_filepath = os.path.normpath(os.getcwd()).split(os.sep)
    test_filepath = os.path.join(os.sep, *test_filepath[:-1], 'test_directory/003434-1-1.nii.gz')

    sys.argv = ['niftiprco', test_filepath]

    niftiprocessing.main()
