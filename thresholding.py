import numpy as np
import pandas as pd
import cv2
import matplotlib.pyplot as plt

original_image = cv2.imread('Diwash.JPG')

# Convert the image in grayscale
img = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)

# Threshold = 120
# All pixels value above threshold will be set to 255
ret, thresh = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY)

# Display
fig, axes = plt.subplots(nrows=1, ncols=2)

imgs = [img, thresh]
for i, ax in enumerate(axes):
    ax.imshow(imgs[i], cmap='gray')
    ax.axis('off')
plt.tight_layout()
plt.show()

# Threshold = 120
thresh = []
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        if img[i][j]> 120: 
            thresh.append(255)
        else:
            thresh.append(0) 

thres_img = np.array(thresh).reshape(img.shape[0],img.shape[1])
fig, axes = plt.subplots(nrows=1, ncols=2)

imgs = [img, thres_img]
for i, ax in enumerate(axes):
    ax.imshow(imgs[i], cmap='gray')
    ax.axis('off')
plt.tight_layout()
plt.show()

# alternate way to display image
# cv2.imshow('Binary Threshold', thresh)

# if cv2.waitKey(0) & 0xff == 27:
# 	cv2.destroyAllWindows()
