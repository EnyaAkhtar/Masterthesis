import os
import pandas as pd

"""
This script edits an existing global lesion metrics file by inserting a column in the beginning containing participant ID.
This is required during neural caudality index (NCI) calculation.
"""

# Path to SPACE-MS output files
metrics_path = "/SPACE-MS/run_sspace_ms/"

# List of all patients
subjects = sorted(os.listdir(metrics_path))

for subject in subjects:
    if not subject.startswith("."):

        # Path to the global lesion metrics
        g_metrics_path = os.path.join(metrics_path, subject, f"{subject}_global_metrics.csv")

        # Read the global lesion metrics into a dataframe
        df = pd.read_csv(g_metrics_path)

        # Insert a column of subjects
        df.insert(0, "Unnamed: 0", [subject])

        # Save edited CSV file
        df.to_csv(os.path.join(metrics_path, subject, f"{subject}_global_metrics_edited.csv"))