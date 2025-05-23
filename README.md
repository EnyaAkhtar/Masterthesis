# Master's Thesis
# Deep Learning in Multiple Sclerosis for MR Lesion Segmentation and Correlation to Symptoms

This repository contains code for segmentation and analysis of brain lesions in multiple sclerosis (MS) patients, in addition to correlation analysis between MS lesions and clinical symptoms.


# Repository structure

## Image processing
This folder contains the scripts describing the preprocessing of the MRI volumes before obtaining MS brain lesions. T1-weighted volumes with contrast and T2-FLAIR volumes were cropped, bias corrected and aligned with each other. Additionally the preprocessed volumes were structured as required by the nnU-Net algorithm. Two Python scripts are included in the folder:

**preprocessing_FSL_anat.py:** 
This script was used to extract the contrast-enhanced T1-weighted volumes and the T2-FLAIR volumes among the different MRI sequences. FSL anat, FSL's anatomical processing pipeline, was used to process both of these volumes. 

**preprocessing_FLIRT.py:**
