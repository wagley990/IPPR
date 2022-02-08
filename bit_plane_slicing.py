import numpy as np
import pandas as pd
import cv2
import matplotlib.pyplot as plt

original_image = cv2.imread('Diwash.jpg')

# Convert the image in grayscale
img = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)

# Iterate over each pixel and change pixel value to binary using np.binary_repr() and store it in a list.
lst = []
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
         lst.append(np.binary_repr(img[i][j] ,width=8)) 
# width = no. of bits
 
# We have a list of strings where each string represents binary pixel value. 
# To extract bit planes, iterate over the strings and store the characters corresponding to bit planes into lists.
# reshape to reconstruct the binary image.
eight_bit_img = (np.array([int(i[0]) for i in lst],dtype = np.uint8)).reshape(img.shape[0],img.shape[1])
seven_bit_img = (np.array([int(i[1]) for i in lst],dtype = np.uint8)).reshape(img.shape[0],img.shape[1])
six_bit_img = (np.array([int(i[2]) for i in lst],dtype = np.uint8)).reshape(img.shape[0],img.shape[1])
five_bit_img = (np.array([int(i[3]) for i in lst],dtype = np.uint8)).reshape(img.shape[0],img.shape[1])
four_bit_img = (np.array([int(i[4]) for i in lst],dtype = np.uint8)).reshape(img.shape[0],img.shape[1])
three_bit_img = (np.array([int(i[5]) for i in lst],dtype = np.uint8)).reshape(img.shape[0],img.shape[1])
two_bit_img = (np.array([int(i[6]) for i in lst],dtype = np.uint8)).reshape(img.shape[0],img.shape[1])
one_bit_img = (np.array([int(i[7]) for i in lst],dtype = np.uint8)).reshape(img.shape[0],img.shape[1])
 
# Concatenate these images for ease of display using cv2.hconcat()
finalr = cv2.hconcat([eight_bit_img,seven_bit_img,six_bit_img,five_bit_img])
finalv =cv2.hconcat([four_bit_img,three_bit_img,two_bit_img,one_bit_img])
 
# Vertically concatenate
final = cv2.vconcat([finalr,finalv])

# Display
fig, axes = plt.subplots(nrows=1, ncols=2)

# cmap maps the color, here we give value 'gray' to cmap for binary image as well bit image, 
# cmap = 'binary' gives negative image
imgs = [img, final]
for i, ax in enumerate(axes):
    ax.imshow(imgs[i], cmap='gray') 
    ax.axis('off')
plt.tight_layout()
plt.show()

lst = []
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
         lst.append(np.binary_repr(img[i][j] ,width=8)) 

plt.figure(figsize = (20, 10))
plt.axis('off')
plt.imshow(final, cmap='gray')
plt.show()