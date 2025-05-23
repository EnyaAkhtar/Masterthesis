import os
import subprocess

def get_transformation_matrix(first, last):

    """
    Get initial transformation matrix by registering a standard MNI brain template to subject space using FLIRT for a subset of MRI volumes in a folder.

    Args:
        first (int): Index of the first patient folder to process.
        last (int): Index of the last patient folder to process.

    Returns:
        None: The function saves the FLIRT output to the specified output directory.

    """

    # Path to standard brain template
    path_standard = "/fsl/data/standard/MNI152_T1_1mm.nii.gz"

    # Path to patient's MRI volumes
    path_subjects = "/input_inference/"

    # Output path to save transformation matrices
    output_path = "/transformation_matrices/"

    # Extract subset of patient volumes
    patient_visits = sorted(os.listdir(path_subjects))[first:last]

    for subject in patient_visits:

        # Get patient ID
        subject_id = subject.split("_")[0] 

        # Specify input and output paths
        subject_path = os.path.join(path_subjects, subject, f"MS_{subject_id}_0001.nii.gz")
        output = os.path.join(output_path, f"{subject}_transformation_matrix.mat")

        # Run FLIRT and get transformation matrices
        print(f"Running FLIRT for {subject}")
        subprocess.run(["flirt",
                        "-in", path_standard,
                        "-ref", subject_path,
                        "-omat", output])

    print(f"{first} to {last} done!")
