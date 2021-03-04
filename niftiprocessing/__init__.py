import argparse
import os

from .nifti import Nifti


def parsercli():
    parser = argparse.ArgumentParser(prog='niftiprocessing')

    # Input
    parser.add_argument('path', type=str, help='Path to file')

    # Input options
    parser.add_argument('--precision', type=int, choices=[32, 64], default=32, help='Sets datatype precision in float32 or 64')

    # Information
    parser.add_argument('--info', '-i', action='store_true', help='Outputs .nii file metadata')
    parser.add_argument('--plot', '-p', type=int, help='Plots image of 2nd/3rd dimension in .nii file (Requires MatplotLib)')

    # Tools
    parser.add_argument('--align', '-a', action='store_true', help='Orients .nii file in MNI152 space')

    parser.add_argument('--normalize', '-n', action='store_true', help='Normalizes .nii file values within set values (Default: 0.,1.)')
    parser.add_argument('--normalize-lower', type=checkintfloat, default=0.0, help='Lower value for normalization (Default: 0.)')
    parser.add_argument('--normalize-upper', type=checkintfloat, default=1.0, help='Lower value for normalization (Default: 0.)')

    parser.add_argument('--rotate', '-r', action='store_true', help='Rotates .nii file by 90 degress in 1st and 2nd dimension')

    parser.add_argument('--output', '-o', action='store_true', help='Filename for .nii file generation (Note: Currently erases orginal metadata)')

    args = parser.parse_args()

    # Initialize Nifti
    niftiobject = Nifti(args.path, args.precision)

    if args.info:
        niftiobject.information()

    if args.align:
        niftiobject.align_nifti()

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
