import os
import subprocess

def running_space_ms(first, last):

    """
    Runs the SPACE-MS algorithm from the script run_sspace_ms.py on a subset of lesion masks in a folder. 

    Args:
        first (int): Index of the first patient folder to process.
        last (int): Index of the last patient folder to process.

    Returns:
        None: The function saves the SPACE-MS output to the specified output directory.
    """

    # Path lesion masks where smallest lesions were removed
    path_filtered_masks = "/masks_small_lesions_removed/" 

    # Path to save SPACE-MS outputs
    output_path = "/SPACE-MS/run_sspace_ms/"

    # Extract masks from the specified subset
    visits = sorted(os.listdir(path_filtered_masks))[first:last] 

    for mask in visits:
        mask_path = os.path.join(path_filtered_masks, mask)

        # Extract patient information
        patient = mask.split(".")[0]       

        # Define output path               
        output = os.path.join(output_path, patient)
        os.makedirs(output, exist_ok=True)
        
        output_name = os.path.join(output, patient)
	
        # Run SPACE-MS on the patient
        print(f"Running sspace_ms for {patient}...") 
        subprocess.run(["python3", "/SPACE-MS/spacetools/run_sspace_ms.py", mask_path, output_name])
