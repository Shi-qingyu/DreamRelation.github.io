from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

# Load the image
img = Image.open('test.png').convert('L')

# Resize the image to 1024x1024 using bilinear interpolation
img_resized = img.resize((1024, 1024), Image.BILINEAR)

# Convert the image to a numpy array
img_array_resized = np.array(img_resized)

# Plot the heatmap with the specified color map (red for max, dark blue for min)
plt.figure(figsize=(10, 10))
plt.imshow(img_array_resized, cmap='jet', interpolation='nearest')
plt.colorbar()
plt.title('Resized Heatmap of the Image (1024x1024)')
plt.axis('off')  # Turn off the axis
plt.show()
