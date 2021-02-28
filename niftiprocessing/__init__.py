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
    parser.add_argument('--info', '-i', action='store_true')
    parser.add_argument('--plot', '-p', type=int)

    # Tools
    parser.add_argument('--denoise', '-d', action='store_true')

    parser.add_argument('--normalize', '-n', action='store_true')
    parser.add_argument('--normalize-lower', type=checkintfloat, default=0.0)
    parser.add_argument('--normalize-upper', type=checkintfloat, default=1.0)

    parser.add_argument('--rotate', '-r', action='store_true')

    parser.add_argument('--output', '-o', action='store_true')

    args = parser.parse_args()

    # Initialize Nifti
    niftiobject = Nifti(args.path, args.precision)

    if args.info:
        niftiobject.information()

    if args.normalize:
        niftiobject.normalize_nifti(args.normalize_lower, args.normalize_upper)

    if args.rotate:
        niftiobject.rotate_nifti()

    if args.plot:
        niftiobject.plot(args.plot)

    if args.output:
        niftiobject.write_nifti()


def checkintfloat(x):
    if not (type(x) == float or type(x) == int):
        TypeError('Input(s) for --normalize must be an int or float')

    return float(x)


def main():
    parsercli()
