import pydicom
import os
import numpy as np
import matplotlib.pyplot as plt

# Path to one patient folder
patient_folder = "images/TCGA-COAD/TCGA-AY-4070A/12-02-1997-NA-CT ABDOMEN PELVIS W CONT-75829/2.000000-AbdomenPelv  5.0  B30f-00432"

# Load all DICOM slices
slices = [pydicom.dcmread(os.path.join(patient_folder, f))
          for f in os.listdir(patient_folder) if f.endswith('.dcm')]

# Sort slices by z position
slices.sort(key=lambda x: float(x.ImagePositionPatient[2]))

# Stack into 3D array
volume = np.stack([s.pixel_array for s in slices])
print(volume.shape)  # e.g. (100, 512, 512)

# Show one slice
plt.imshow(volume[50], cmap='gray')
plt.title("Mid slice")
plt.axis('off')
plt.show()
