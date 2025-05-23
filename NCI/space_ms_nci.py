import os
import subprocess

def run_space_ms_caudality(first, last):

    """
    Computes the neural caudality index (NCI) using the supplementary motor area (SMA) and brainstem parcellations 
    in addition to the SPACE-MS outputs. The lesion metrics and global lesion metrics from SPACE-MS are required to run the script,
    in addition to a CSV file to paths of labelled lesion masks and labelled parcellations. The labels of the SMA and brainstem
    need to be specified when running the script. 

    Args:
        first (int): Index of the first patient folder to process.
        last (int): Index of the last patient folder to process.

    Returns:
        None: The function computes NCI metrics and saves them in the specified directory.    
    """

    # Path to the input CSV files containing lesion mask and parcellation paths
    input_csv_files = "/SPACE-MS/MS_SMART/input_csv/"

    # Path to the SPACE-MS output files
    metric_files = "/SPACE-MS/run_sspace_ms/"

    # Output path to save NCI metrics
    output_path = "/SPACE-MS/MS_SMART/MS_SMART_results/"

    # Path to code for computing NCI metrics
    algorithm_path = "/part2_spacems_caudality.py/part2_spacems_caudality_edited.py"

    for file in sorted(os.listdir(input_csv_files))[first:last]:

        # Get subject from file
        csv_file = os.path.join(input_csv_files, file)
        subject = file.split(".")[0]

        # Paths to the lesion metrics and global lesion metrics from SPACE-MS
        global_metrics = os.path.join(metric_files, subject, f"{subject}_global_metrics_edited.csv")
        lesion_metrics = os.path.join(metric_files, subject, f"{subject}_lesion_metrics.csv")
        
        # Define output path
        output = os.path.join(output_path, subject)

        # Run the NCI-algorithm
        subprocess.run(["python3", algorithm_path,
                        "-i", csv_file,
                        "-sma", '1', '1',               # SMA label and parameter
                        "-bs", '2',                     # Brainstem label
                        "-g_metrics", global_metrics,
                        "-l_metrics", lesion_metrics,
                        "-o", output])


