import glob
import cv2
import numpy as np
from PIL import Image

# read all images and normalise them and save them in an array
I = np.zeros((550, 430, 12))
i = 0
for img in glob.glob('objects/*.png'):
    picture = np.array(Image.open(img), 'f')
    I[:, :, i] = picture
    i += 1

# use 99 as suggested in the MATLAB implementation
I_normalized = I/99

# create a shadow mask
shadow_threshold = 0.1
n_image = I_normalized.shape[2]
shadow_mask = I_normalized > shadow_threshold


# produce a kernel similar to the strel('disk', radius) in MATLAB
def strel_python(radius):
    kernel = np.zeros((2*radius-1, 2*radius-1), np.uint8)
    y, x = np.ogrid[-radius+1:radius, -radius+1:radius]
    mask = x**2 + y**2 <= (radius-1)**2
    kernel[mask] = 1
    kernel[0, radius-1:kernel.shape[1]-radius+1] = 1
    kernel[kernel.shape[0]-1, radius-1:kernel.shape[1]-radius+1]= 1
    kernel[radius-1:kernel.shape[0]-radius+1, 0] = 1
    kernel[radius-1:kernel.shape[0]-radius+1, kernel.shape[1]-1] = 1
    return kernel


# save shadow masks for each image
kernel = strel_python(5)
for i in range(n_image):
    shadow_mask[:, :, i] = cv2.erode(shadow_mask[:, :, i].astype(np.uint8), kernel)
    Image.fromarray(shadow_mask[:, :, i]).save('masks/shadow_mask_' + str(i+1).zfill(2) + '.png')
