import argparse
import os

from .nifti import Nifti


def parsercli():
    parser = argparse.ArgumentParser(prog='niftiprocessing')

    # Input
    parser.add_argument('path', type=str, help='Path to file or directory')

    # Input options
    parser.add_argument('--precision', type=int, choices=[32, 64], default=32)

    # Information
    parser.add_argument('-info', '-i', action='store_true')

    # Tools
    parser.add_argument('--denoise', '-d', action='store_true')

    args = parser.parse_args()

    # Initialize Nifti
    niftiobject = Nifti(args.path, args.precision)

    # Test arguments
    print(args.path)
    print(args.precision)

    if args.info:
        niftiobject.information()


def main():
    parsercli()
