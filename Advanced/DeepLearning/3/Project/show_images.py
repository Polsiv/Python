import os
import numpy as np
import pandas as pd
import pydicom
import matplotlib.pyplot as plt
from scipy.ndimage import zoom    

# -----------------------------------------------------------
# Display slices
# -----------------------------------------------------------
def plot_slices(volume, num_rows=4, num_cols=8):
    num_slices = num_rows * num_cols
    depth = volume.shape[0]

    plt.rcParams.update({
        'text.usetex': True,               # use LaTeX for all text
        'font.family': 'serif',            # use a serif font (LaTeX default)
        'font.serif': ['Computer Modern'], # optional, but matches LaTeX’s default
        'font.size': 15,
        })

    indices = np.linspace(0, depth - 1, num_slices, dtype=int)
    fig, axes = plt.subplots(num_rows, num_cols, figsize=(12, 6))

    for i, ax in enumerate(axes.flat):
        if i < len(indices):
            slice_img = volume[indices[i], :, :]
            ax.imshow(slice_img, cmap="gray")
            ax.axis("off")
            ax.set_title(f"z={indices[i]}")

    plt.suptitle("Stage IV Volume Sizes", fontsize=20)
    plt.tight_layout()
    plt.show()


# -----------------------------------------------------------
# Load a folder of DICOM files into a 3D NumPy volume
# -----------------------------------------------------------
def load_dicom_volume(folder_path):
    dicom_files = [
        pydicom.dcmread(os.path.join(folder_path, f))
        for f in os.listdir(folder_path)
        if f.endswith(".dcm")
    ]

    # Sort by Z position
    dicom_files.sort(key=lambda dcm: float(dcm.ImagePositionPatient[2]))

    # Build slices using your method
    slices = []
    for dcm in dicom_files:
        img = dcm.pixel_array.astype(np.float32)

        # Apply HU conversion
        if hasattr(dcm, "RescaleSlope") and hasattr(dcm, "RescaleIntercept"):
            img = img * float(dcm.RescaleSlope) + float(dcm.RescaleIntercept)

        slices.append(img)

    # Stack into (depth, height, width)
    volume = np.stack(slices, axis=0)
    return volume



# -----------------------------------------------------------
# Apply Hounsfield normalization + resizing
# -----------------------------------------------------------
def preprocess_volume(volume, target_size=(64, 224, 224)):
    # ----- 1. Window to [-1000, 400]
    volume = np.clip(volume, -1000, 400)

    # ----- 2. Normalize to [0,1]
    volume = (volume + 1000) / 1400.0

    # ----- 3. Resize to target shape
    zoom_factors = (
        target_size[0] / volume.shape[0],
        target_size[1] / volume.shape[1],
        target_size[2] / volume.shape[2],
    )
    volume = zoom(volume, zoom_factors, order=1)   # linear interpolation

    return volume


# -----------------------------------------------------------
# Main pipeline
# -----------------------------------------------------------
def main():
    # Load CSV
    df = pd.read_csv("datasets/colorectal_ct_patients.csv")
    ct_folders = df["ct_folder_path"]

    # Choose patient
    patient = 110
    folder = ct_folders[patient]
    print(f"Loading CT volume from: {folder}")

    # Load raw CT
    volume = load_dicom_volume(folder)
    print("Original shape:", volume.shape)

    # Preprocess CT (window, normalize, resize)
    volume = preprocess_volume(volume, target_size=(128, 256, 256))
    print("Processed shape:", volume.shape)

    # Plot sample slices
    plot_slices(volume)


if __name__ == "__main__":
    main()
