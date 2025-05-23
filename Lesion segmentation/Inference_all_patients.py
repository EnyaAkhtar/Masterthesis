import os
import subprocess

"""
Running nnU-Net inference on a folder of MRI volumes.

For each patient folder in the specified input directory, this script runs nnUNet_predict
using the full-resolution 3D model trained on a multiple sclerosis task, and saves 
the predicted lesion masks in the corresponding output folder.
"""

# Path to input data
inference_input_path = "/input_inference" 

# Path to save lesion masks
inference_outputs = "/output_inference"   

for patient_visit in os.listdir(inference_input_path):

    # Full path to the patient folder
    sequence = os.path.join(inference_input_path, patient_visit)

    # Full output path
    patient_output_path = os.path.join(inference_outputs, patient_visit)
    os.makedirs(patient_output_path, exist_ok=True)

    print(f"Running inference on {patient_visit}...")

    # Run inference on patients and save in specified folder
    subprocess.run([
        "nnUNet_predict",
        "-i", sequence,
        "-o", patient_output_path,  
        "-tr", "nnUNetTrainerV2",
        "-ctr", "nnUNetTrainerV2CascadeFullRes",
        "-m", "3d_fullres",
        "-p", "nnUNetPlansv2.1",
        "-t", "Task555_MultipleSclerosis"
    ])

print("INFERENCE COMPLETE!")

