import os
import subprocess

def apply_warp(first, last):

    """
    Applies non-linear warp fields (from FNIRT) to standard cortical and subcortical atlases, transforming them into subject space.


    Args:
        first (int): Index of the first patient folder to process.
        last (int): Index of the last patient folder to process.

    Returns:
        None: The warped atlases are saved to the specified output directories.
    """

    # Path to standard atlas of cortical structures
    path_cortical_atlas = "/fsl/data/atlases/HarvardOxford/HarvardOxford-cort-maxprob-thr50-1mm.nii.gz"
    
    # Path to standard atlas of subcortical structures
    path_subcortical_atlas = "/fsl/data/atlases/HarvardOxford/HarvardOxford-sub-maxprob-thr50-1mm.nii.gz"
    
    # Path to warp fields after running FNIRT
    path_warp_fields = "/warp_fields/"
    
    # Path to MRI volumes
    path_subjects = "/input_inference/"
    
    # Output path for cortical and subcortical masks in subject space
    cortical_output_path = "/applied_atlas/cortical_sma/"
    subcortical_output_path = "/applied_atlas/subcortical_brainstem/"

    patient_visits = sorted(os.listdir(path_subjects))[first:last]

    for subject in patient_visits:

        # Define patient ID and paths
        subject_id = subject.split("_")[0] 
        subject_path = os.path.join(path_subjects, subject, f"MS_{subject_id}_0001.nii.gz")

        warp_field = os.path.join(path_warp_fields, f"{subject}_warp_field.nii.gz")

        output_cortical = os.path.join(cortical_output_path, f"{subject}_cortical_atlas.nii.gz")
        output_subcortical = os.path.join(subcortical_output_path, f"{subject}_subcortical_atlas.nii.gz")

        # Apply warp field on the cortical atlas 
        print(f"Running applywarp for {subject} - CORTICAL ATLAS")
        subprocess.run(["applywarp",
                        f"--in={path_cortical_atlas}",
                        f"--ref={subject_path}",
                        f"--warp={warp_field}",
                        f"--out={output_cortical}",
                        "--interp=nn"])

        # Apply warp field to subcortical atlas
        print(f"Running applywarp for {subject} - SUBCORTICAL ATLAS")
        subprocess.run(["applywarp",
                        f"--in={path_subcortical_atlas}",
                        f"--ref={subject_path}",
                        f"--warp={warp_field}",
                        f"--out={output_subcortical}",
                        "--interp=nn"])

    print(f"{first} to {last} done!")
