import os
import SimpleITK as sitk

from .numpyhelper import normalize, rotate_image
from .graphical import plot_slice
from .niftihelper import align


class Nifti:

    def __init__(self, filepath: str, precision: int):
        dtype = sitk.sitkFloat32 if precision == 32 else sitk.sitkFloat64

        sitk_image = sitk.ReadImage(filepath, dtype)

        self.nifti_array = sitk.GetArrayFromImage(sitk_image)
        self.file_name = os.path.basename(filepath)
        self.filepath = filepath
        self.reader = sitk.ImageFileReader()

    def information(self):
        print(f'--{self.file_name}--')
        print(f'Shape: {self.nifti_array.shape}')

        self.reader.SetFileName(self.filepath)
        self.reader.LoadPrivateTagsOn()

        self.reader.ReadImageInformation()

        for k in self.reader.GetMetaDataKeys():
            v = self.reader.GetMetaData(k)
            if not (v == '0' or v == ''):
                print(f"({k}) == \"{v}\"")

    def plot(self, slice_index: int):
        plot_slice(self.nifti_array, slice_index)

    def align_nifti(self):
        self.nifti_array = align(self.nifti_array, self.reader)

    def normalize_nifti(self, lower: float, upper: float):
        self.nifti_array = normalize(self.nifti_array, lower, upper)

    def rotate_nifti(self):
        self.nifti_array = rotate_image(self.nifti_array)

    def write_nifti(self):
        output = sitk.GetImageFromArray(self.nifti_array)

        output_path = os.path.join(os.getcwd(), 'test.nii.gz')

        sitk.WriteImage(output, output_path)