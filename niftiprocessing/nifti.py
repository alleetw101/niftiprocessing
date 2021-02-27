import numpy as np
import os
import SimpleITK as sitk

from .numpyhelper import normalize

class Nifti:

    def __init__(self, filepath: str, precision: int):
        dtype = sitk.sitkFloat32 if precision == 32 else sitk.sitkFloat64

        self.nifti_array = sitk.GetArrayFromImage(sitk.ReadImage(filepath, dtype))

        self.shape = self.nifti_array.shape
        self.file_name = os.path.basename(filepath)
        self.filepath = filepath

    def information(self):
        print(f'--{self.file_name}--')
        print(f'Shape: {self.shape}')

        reader = sitk.ImageFileReader()

        reader.SetFileName(self.filepath)
        reader.LoadPrivateTagsOn()

        reader.ReadImageInformation()

        for k in reader.GetMetaDataKeys():
            v = reader.GetMetaData(k)
            if not (v == '0' or v == ''):
                print(f"({k}) == \"{v}\"")

    def normalize_nifti(self, lower: float, upper: float):
        self.nifti_array = normalize(self.nifti_array, lower, upper)
