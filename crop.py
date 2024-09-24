# https://stackoverflow.com/questions/72887400/install-gdal-on-linux-ubuntu-20-04-4lts-for-python
from osgeo import gdal
import sys
import matplotlib.pyplot as plt
import cv2
import numpy as np

# Open the source dataset
src_ds = gdal.Open(

)
if src_ds is None:
    print("Unable to open the dataset.")
    sys.exit(1)

# Get the first raster band
rb = src_ds.GetRasterBand(1)
img_array = rb.ReadAsArray()

# Check if the image is in the correct format for equalization
if img_array.dtype != np.uint8:
    # Normalize and convert to uint8
    img_normalized = cv2.normalize(img_array, None, 0, 255, cv2.NORM_MINMAX)
    img_uint8 = img_normalized.astype(np.uint8)
else:
    img_uint8 = img_array

# Apply histogram equalization
equ = cv2.equalizeHist(img_uint8)
print(equ.shape)
# Display the original and equalized images
plt.figure(figsize=(12, 6))

# Original Image
plt.subplot(1, 2, 1)
plt.title("Original Image")
plt.imshow(equ, cmap="gray")
plt.axis("off")

# cropped image
cropped_image = equ[10000:20000, 10000:20000]
plt.subplot(1, 2, 2)
plt.title("Cropped Image")
plt.imshow(cropped_image, cmap="gray")
plt.axis("off")

plt.show()
