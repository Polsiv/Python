import pydicom
import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import pandas as pd

def main():
    df = pd.read_csv("datasets/colorectal_ct_patients.csv")
    ct_folders = df["ct_folder_path"]
    patient = 400
    patient_folder = ct_folders[patient]


    # Load all DICOM slices
    slices = [pydicom.dcmread(os.path.join(patient_folder, f))
            for f in os.listdir(patient_folder) if f.endswith('.dcm')]

    # Sort slices by z position
    slices.sort(key=lambda x: float(x.ImagePositionPatient[2]))

    # Stack into 3D array
    volume = np.stack([s.pixel_array for s in slices])
    print(f"Volume shape: {volume.shape}")  

    # Create animation
    fig, ax = plt.subplots(figsize=(8, 8))
    im = ax.imshow(volume[0], cmap = 'gray')
    ax.axis('off')
    plt.title("Slice 0")

    def update(frame):
        im.set_array(volume[frame])
        ax.set_title(f"Slice {frame}/{len(volume)-1}")
        return [im]

    # Create animation - adjust interval for speed (milliseconds)
    anim = FuncAnimation(fig, update, frames=len(volume), 
                        interval=50, blit=True)

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()