import os
import subprocess
import nibabel as nib
import numpy as np

def get_parcellation():

    """
    Get masks consisting of supplementary motor area (SMA) and brainstem from the subject specific cortical and subcortical atlases. 

    Returns:
        None: SMA and brainstem parcellation masks are generated and saved in a specified directory.
    """

    # Path to cortical atlas in subject space
    cortical_atlas = "/applied_atlas/cortical_sma/"
    
    # Path to subcortical atlas in subject space
    subcortical_atlas = "/applied_atlas/subcortical_brainstem/"
    
    # Output path to save generated masks
    output_path = "/sma_brainstem_parcellations/"
    
    # Path to MR volumes
    path_subjects = "/input_inference/"

    patient_visits = sorted(os.listdir(path_subjects))

    for subject in patient_visits:
        
        # Full paths to patient specific atlases
        cortical_path = os.path.join(cortical_atlas, f"{subject}_cortical_atlas.nii.gz")
        subcortical_path = os.path.join(subcortical_atlas, f"{subject}_subcortical_atlas.nii.gz")

        # Load atlases
        brainstem_tot = nib.load(subcortical_path).get_fdata()
        sma_tot = nib.load(cortical_path).get_fdata()

        # Extract SMA and brainstem parcellations
        sma_mask = sma_tot == 26
        brainstem_mask = brainstem_tot == 8

        # Initialize new mask
        parcellations = np.zeros_like(sma_mask, dtype=np.uint8)

        # Assign label 1 to SMA region
        parcellations[sma_mask] = 1  

        # Assign label 2 to brainstem region
        parcellations[brainstem_mask] = 2  

        # Save masks as NIfTI files
        parcellation_mask = nib.Nifti1Image(parcellations, nib.load(cortical_path).affine, nib.load(cortical_path).header)
        output = os.path.join(output_path, f"{subject}_parcellation.nii")
        nib.save(parcellation_mask, output)

        