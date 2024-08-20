import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image provided by the user
image_path = "image.png"  # แก้ไข path เป็น path ของไฟล์ที่ถูกต้อง
image = cv2.imread(image_path)

# Define the region of interest (ROI) for the UI at the bottom of the screen
# Adjust the values to fit the 1600x900 resolution
roi = image[700:1000, 720:1200]  # Adjusted ROI to capture the correct region

# Convert the ROI from BGR (OpenCV) to RGB (Matplotlib)
roi_rgb = cv2.cvtColor(roi, cv2.COLOR_BGR2RGB)

# Define the approximate BGR color range for the blue highlight
lower_blue = np.array([100, 50, 50])
upper_blue = np.array([130, 255, 255])

# Create a mask to detect blue areas
mask = cv2.inRange(roi, lower_blue, upper_blue)

# Display the result
plt.figure(figsize=(6, 3))
plt.imshow(roi_rgb)

plt.show()
