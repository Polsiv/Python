import pandas as pd
from pathlib import Path
import os

def create_patient_csv(stage2_root, stage4_root, output_csv="colorectal_ct_patients.csv"):
    patients_data = []
    
    # Process Stage 2 dataset
    stage2_path = Path(stage2_root)
    print(f"Looking for Stage 2 patients in: {stage2_path}")
    
    for patient_folder in stage2_path.iterdir():
        if patient_folder.is_dir():
            print(f"Found Stage 2 folder: {patient_folder.name}")
            ct_folder = find_ct_slices_folder(patient_folder)
            if ct_folder:
                patients_data.append({
                    'patient_id': patient_folder.name,
                    'ct_folder_path': str(ct_folder),
                    'stage': 2,
                    'dataset_source': 'stage2',
                    'num_slices': count_dicom_files(ct_folder)
                })
                print(f"  Added: {patient_folder.name} with {count_dicom_files(ct_folder)} slices")
            else:
                print(f"  No CT slices found in: {patient_folder.name}")
    
    # Process Stage 4 dataset
    stage4_path = Path(stage4_root)
    print(f"\nLooking for Stage 4 patients in: {stage4_path}")
    
    for patient_folder in stage4_path.iterdir():
        if patient_folder.is_dir():

            print(f"Found Stage 4 folder: {patient_folder.name}")
            ct_folder = find_ct_folder_stage4(patient_folder)

            if ct_folder:
                
                patients_data.append({
                    'patient_id': patient_folder.name,
                    'ct_folder_path': str(ct_folder),
                    'stage': 4,
                    'dataset_source': 'stage4',
                    'num_slices': count_dicom_files(ct_folder)
                })
                print(f"  Added: {patient_folder.name} with {count_dicom_files(ct_folder)} slices")
                
            else:
                print(f"  No CT slices found in: {patient_folder.name}")
    
    # Create DataFrame and save
    df = pd.DataFrame(patients_data)
    df.to_csv(output_csv, index=False)
    print(f"\nCreated CSV with {len(df)} patients")
    print(f"Stage 2 patients: {len(df[df['stage'] == 2])}")
    print(f"Stage 4 patients: {len(df[df['stage'] == 4])}")
    return df

def find_ct_slices_folder(patient_folder):
    """Find the folder containing CT slices (many .dcm files) in Stage 2 structure"""
    # For Stage 2: patient_folder/date-NA-studyID/series-folder/
    for study_folder in patient_folder.iterdir():
        if study_folder.is_dir():
            for series_folder in study_folder.iterdir():
                if series_folder.is_dir():
                    dcm_files = list(series_folder.glob("*.dcm"))
                    if len(dcm_files) > 10:  # CT volume has many slices
                        return series_folder
    return None

def find_ct_folder_stage4(patient_folder):
    """For Stage 4, find CT folder (not segmentation folder)"""
    # For Stage 4: patient_folder/date-NA-studyID/
    # Contains both "100.000000-Segmentation-XXXX" and "101.000000-NA-XXXX"
    for study_folder in patient_folder.iterdir():
        if study_folder.is_dir():
            for series_folder in study_folder.iterdir():
                if series_folder.is_dir():
                    # Look for folder that's NOT segmentation
                    if "Segmentation" not in series_folder.name:
                        dcm_files = list(series_folder.glob("*.dcm"))
                        if len(dcm_files) > 10:  # CT volume
                            return series_folder
    return None

def count_dicom_files(folder_path):
    """Count how many DICOM files are in a folder"""
    return len(list(Path(folder_path).glob("*.dcm")))

# Usage with your paths:
df = create_patient_csv(
    stage2_root="images/Stage2/StageII-Colorectal-CT",
    stage4_root="images/Stage4/Colorectal-Liver-Metastases", 
    output_csv="colorectal_ct_patients.csv"
)

# Display sample of the created CSV
print("\nSample of created CSV:")
print(df.head())