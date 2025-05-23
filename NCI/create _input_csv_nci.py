import os
import subprocess
import nibabel as nib
import numpy as np


def create_input_csv():

    """
    Creates a CSV file of paths to the labelled lesion masks and parcellation masks containing 
    supplementary motor area (SMA) and brainstem parcellations. This file is required during neural
    caudality index (NCI) computation.

    Returns:
        None: CSV files are saved in specified directories.

    """

    # Path to supplementary motor area (SMA) and brainstem masks 
    parcellations_path = "/SPACE-MS/MS_SMART/create_parcellations/sma_brainstem_parcellations/"

    # Path to SPACE-MS output files
    basal_masks_path = "/SPACE-MS/run_sspace_ms/"

    # Output folder to save generated CSV files
    output_path = "/SPACE-MS/MS_SMART/input_csv/"

    # List of all patient masks
    basal_masks_subjects = sorted(os.listdir(basal_masks_path))

    for subject in basal_masks_subjects:
        if not subject.startswith('.'):
            
            # Path to subject specific labelled lesion masks
            lab_les_path = os.path.join(basal_masks_path, subject, f"{subject}_lesion_labels.nii")
            
            # Path to subject specific SMA and brainstem masks
            parc_path = os.path.join(parcellations_path, f"01-{subject}_parcellation.nii")

            # Dataframe of paths to the labelled lesion masks and parcellation masks
            df = pd.DataFrame({"lab_les":[lab_les_path], "parcellations":[parc_path]})
            
            # Save the dataframe as a CSV in the output folder
            output = os.path.join(output_path, f"{subject}.csv")
            df.to_csv(output, index = False)

        print(f"csv for {subject} saved")