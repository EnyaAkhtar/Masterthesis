import os
import subprocess

def get_warp_field(first, last):

    """
    Get warp fields through non-linear registration using FNIRT on a subset of MR volumes. 
    Initial transfrmations are used by utilizing output from FLIRT.
 
    Args:
        first (int): Index of the first patient folder to process.
        last (int): Index of the last patient folder to process.

    Returns:
        None: The function saves the FNIRT output to the specified output directory.   
    
    """

    # Path to standard brain template
    path_standard = "/fsl/data/standard/MNI152_T1_1mm.nii.gz"
    
    # Path to MRI volumes
    path_subjects = "/input_inference/"

    # Path to the initial transformation matrices from running FLIRT
    transformation_path = "/transformation_matrices/"

    # Output path to save warp fields
    output_path = "/warp_fields/"

    # Extract subset of patient volumes
    patient_visits = sorted(os.listdir(path_subjects))[first:last]

    for subject in patient_visits:

        # Get patient ID and specify paths
        subject_id = subject.split("_")[0] 
        subject_path = os.path.join(path_subjects, subject, f"MS_{subject_id}_0001.nii.gz")

        transformation_matrix = os.path.join(transformation_path, f"{subject}_transformation_matrix.mat")
        output = os.path.join(output_path, f"{subject}_warp_field.nii.gz")

        # Run FNIRT to get warp fields
        print(f"Running FNIRT for {subject}")
        subprocess.run(["fnirt",
                        f"--in={path_standard}",
                        f"--ref={subject_path}",
                        f"--aff={transformation_matrix}",
                        f"--cout={output}"])

    print(f"{first} to {last} done!")
