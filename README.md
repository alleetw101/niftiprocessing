# NiftiProcessing

A nifti file processing tool

Under development

This software has NOT been approved for medical analysis/diagnosis. Please use other
approved software for medical use.

# Options
    positional arguments:
      path                  Path to file
    
    optional arguments:
      -h, --help            show this help message and exit
      --precision {32,64}   Sets datatype precision in float32 or 64
      --info, -i            Outputs .nii file metadata
      --plot PLOT, -p PLOT  Plots image of 2nd/3rd dimension in .nii file 
                            (Requires MatplotLib)
      --align, -a           Orients .nii file in MNI152 space
      --normalize, -n       Normalizes .nii file values within set values 
                            (Default: 0.,1.)
      --normalize-lower     Lower value for normalization (Default: 0.)
      --normalize-upper     Lower value for normalization (Default: 0.)
      --rotate, -r          Rotates .nii file by 90 degress in 1st and 2nd dimension
      --output, -o          Filename for .nii file generation 
                            (Note: Currently erases orginal metadata)

# Usage Examples
```bash
# Orients nifti file to MNI152 space
$ niftiprocessing sample.nii.gz -a -o output.nii.gz

# Plot slice 150 with matplotlib
$ niftiprocessing sample.nii.gz -p 150
```

## Actions to implement:

Input
- Single
- Batch (directory)

Tools
- resize
- resize with pad
- resize with crop
- flip
- rotate
- invert
- denoise
- normalize
- align

Information
- scan information

Visualize
- terminal drawing output for orientation

Output
- Single
- Batch (directory)
