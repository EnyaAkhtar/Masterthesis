# Master's Thesis
# Deep Learning in Multiple Sclerosis for MR Lesion Segmentation and Correlation to Symptoms

This repository contains code for segmentation and analysis of brain lesions in multiple sclerosis (MS) patients, in addition to correlation analysis between MS lesions and clinical symptoms.

## Table of Contents

- [Image processing](#Image processing)
- [Lesion segmentation](#Lesion segmentation)


# Repository structure

# Image processing

This folder consists of scripts describing the performed preprocessing of the MRI volumes before obtaining MS brain lesions. T1-weighted volumes with contrast and T2-FLAIR volumes were cropped, bias corrected and aligned with each other. Additionally the preprocessed volumes were structured as required by the nnU-Net algorithm. Two Python scripts are included in the folder.

**preprocessing_FSL_anat.py:** 

This script was used to extract the contrast-enhanced T1-weighted volumes and the T2-FLAIR volumes among the different MRI sequences. FSL anat, FSL's anatomical processing pipeline, was used to process both of these volumes. 

**preprocessing_FLIRT.py:**

This script extracts the scaled and bias corrected volumes from the FSL anat outputs. The T2-FLAIR volumes were registered to the T1-weighted volumes using FSL's FLIRT. Subsequently, the T1 volumes and registered T2 volumes were renamed and the folders were structured to prepare for running nnU-Net inference.

# Lesion segmentation

This folder contains the code used for lesion segmentation of T2 lesions and T1 lesions (black holes). Binary lesion masks were segmented using thresholding and deep learning based methods. 

### T2 lesions

**inference_all_patients.py:**

The T2 lesion masks were obtained by using a pretrained nnU-Net model and running inference on the preprocessed data. 

### T1 lesions

**T1-lesions_thresholding.ipynb**

This notebook consists of the code which was used to extract T1 lesions from T2 lesions through a threshold-based approach. The threshold was set as the 5th percentile of the grey matter intensity, and the tissue segmentation acquired from FSL anat was therefore used. All T2 lesion voxels that had an intensity lower than the threshold were classified as T1 lesion voxels. 

**3D-U-NET_T1_segmentation.ipynb**

The T1 lesion masks obtained from thresholding were used as ground truth labels in a deep learning pipeline for automated T1 lesion segmentation. Two U-Net frameworks were trained using different hyperparameter combinations. The U-Net frameworks were similar, but differed in their required input channels, where one relied solely on T1-weighted volumes as input, while the other also used T2-lesion masks. This notebook describes the data preparation, training, model selection and evaluation of these networks.
