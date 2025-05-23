import os
import subprocess


def run_fsl_anat(first, last):

    """
    Runs FSL's anatomical processing (FSL anat) on contrast-enhanced T1-weighted and T2-FLAIR volumes 
    for a subset of patients.

    Args:
        first (int): Index of the first patient folder to process.
        last (int): Index of the last patient folder to process.

    Returns:
        None: The function saves the FSL anat output to the specified output directory.
    """


    # Path to the patient data
    data_path = "/Data/Overlord_anon_new"

    # Output path to save processed files
    output_path = '/fsl_preprocessed'


    # Walk through the patient data 
    for root, dirs, files in list(os.walk(data_path))[first:last]:
        t1_path = None
        t2_path = None

        for file in files:

            # Find the correct T2-FLAIR and T1 weighted volumes
            if '_t2_spc_da-fl_sag_HF_p3_' in file and file.endswith('spcir_278ns.nii.gz') and  '_ND_' not in file and 'registered' not in file:
                t2_path = os.path.join(root, file)

            if '_t1_mprage_sag_1mm_iso_+K' in file and file.endswith('.nii.gz') and 'quarantine' not in root:
                t1_path = os.path.join(root, file)

        if t1_path and t2_path:

            # Extract patient name, given as 01_XXX_visit_X
            patient_name = root.split('/')[-1]

            # Define an output directory based on patient name
            output_folder = os.path.join(output_path, patient_name)
            os.makedirs(output_folder, exist_ok=True)

            # Define the output path name for both modalities
            t2_output_path = os.path.join(output_folder, t2_path.split('/')[-1])
            t1_output_path = os.path.join(output_folder, t1_path.split('/')[-1])

            # Run FSL anat on the volumes and save to specified folders
            print(f"Processing {patient_name}, T2-FLAIR ...")
            subprocess.run(["FSL anat", "-i", t2_path, "-o", t2_output_path, "-t", "T2", "--nononlinreg", "--nosubcortseg"])

            print(f"Processing {patient_name}, T1 ...")
            subprocess.run(["FSL anat", "-i", t1_path, "-o", t1_output_path])

    print("All sequences processed!")


