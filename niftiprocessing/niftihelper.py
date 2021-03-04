import numpy as np


def align(array, reader):
    nifti_array = array
    alignment_matrix = [reader.GetMetaData('srow_x').split()[:3], reader.GetMetaData('srow_y').split()[:3],
                        reader.GetMetaData('srow_z').split()[:3]]

    for row in range(len(alignment_matrix)):
        for col in range(len(alignment_matrix[0])):
            alignment_matrix[row][col] = int(round(float(alignment_matrix[row][col])))

    flip_list = [sum(x) for x in zip(alignment_matrix[0], alignment_matrix[1], alignment_matrix[2])]

    for position in range(len(flip_list)):
        if flip_list[position] < 0:
            nifti_array = np.flip(nifti_array, axis=position)

    for row in range(len(alignment_matrix)):
        for col in range(len(alignment_matrix[0])):
            alignment_matrix[row][col] = abs(alignment_matrix[row][col])

    if abs(alignment_matrix[0][0]) != 1:
        tranpose_list = [0, 1, 2]
        for index in range(len(alignment_matrix)):
            if alignment_matrix[index][0] == 1:
                swap_index = index
                break
        tranpose_list[swap_index], tranpose_list[0] = tranpose_list[0], tranpose_list[swap_index]
        alignment_matrix[swap_index], alignment_matrix[0] = alignment_matrix[0], alignment_matrix[swap_index]

        nifti_array = np.transpose(nifti_array, tranpose_list)
        nifti_array = np.flip(nifti_array, axis=swap_index)

    if abs(alignment_matrix[1][1]) != 1:
        tranpose_list = [0, 1, 2]
        for index in range(len(alignment_matrix)):
            if alignment_matrix[index][1] == 1:
                swap_index = index
                break
        tranpose_list[swap_index], tranpose_list[1] = tranpose_list[1], tranpose_list[swap_index]
        alignment_matrix[swap_index], alignment_matrix[1] = alignment_matrix[1], alignment_matrix[swap_index]

        nifti_array = np.transpose(nifti_array, tranpose_list)
        nifti_array = np.flip(nifti_array, axis=swap_index)

    if abs(alignment_matrix[2][2]) != 1:
        tranpose_list = [0, 1, 2]
        for index in range(len(alignment_matrix)):
            if alignment_matrix[index][2] == 1:
                swap_index = index
                break
        tranpose_list[swap_index], tranpose_list[2] = tranpose_list[2], tranpose_list[swap_index]
        alignment_matrix[swap_index], alignment_matrix[2] = alignment_matrix[2], alignment_matrix[swap_index]

        nifti_array = np.transpose(nifti_array, tranpose_list)
        nifti_array = np.flip(nifti_array, axis=swap_index)

    return nifti_array
