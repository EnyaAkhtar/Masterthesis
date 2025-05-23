import os
import shutil
import subprocess


def run_flirt(first, last):        
    """
    Registers the bias corrected T2-FLAIR volume to the T1-weighted volume using FSL's FLIRT tool, 
    and prepares the output directory structure for nnU-Net inference.

    Args:
        first (int): Index of the first patient folder to process.
        last (int): Index of the last patient folder to process.

    Returns:
        None: Registered images are saved to the output directory in nnU-Net-compatible format.
    """

    # The input and output paths
    input_path = '/fsl_preprocessed'
    output_path = '/input_inference'

    # Specified subset of patient folders
    subjects = sorted(os.listdir(input_path))[first:last]

    for patient_visit in subjects:

        # Full path to the patient and extract patient ID
        patient_path = os.path.join(input_path, patient_visit)
        patient_ID = patient_visit.split('_')[0]

        t1_path = None
        t2_path = None

        for mod in os.listdir(patient_path):
            mod_path = os.path.join(patient_path, mod)

            # Find the bias corrected volumes of both modalities
            if '_t2_spc_da-fl_' in mod:
                t2_path = os.path.join(mod_path, "T2_biascorr.nii.gz")

            elif '_t1_mprage_sag_1mm_iso_+K' in mod:
                t1_path = os.path.join(mod_path, "T1_biascorr.nii.gz")

        if t1_path and t2_path:

            # Define output directory structure as required by nnU-Net
            t2_name = f"MS_{patient_ID}_0000.nii.gz"
            t1_name = f"MS_{patient_ID}_0001.nii.gz"

            inference_path = os.path.join(output_path, patient_visit)
            os.makedirs(inference_path, exist_ok=True)

            t1_output_path = os.path.join(inference_path, t1_name)
            t2_output_path = os.path.join(inference_path, t2_name)

            # Copy T1 volume to the output directory
            shutil.copy(t1_path, t1_output_path)

            # Run FLIRT and save the outcome to the output directory
            print(f"Running FLIRT for {patient_visit}...")

            subprocess.run([
                "flirt",
                "-in", t2_path,
                "-ref", t1_output_path,
                "-out", t2_output_path
            ])

    print("FLIRT processing complete!")
