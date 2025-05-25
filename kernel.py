"""from PIL import Image

image1 = Image.open(r'F:\Chrome Downloads\ITU Internship\lenna.png')
image1.show()
print(image1.size)
"""

import cv2
import numpy as np

original_image = cv2.imread(r'D:\Assignments\images.jfif', cv2.IMREAD_GRAYSCALE)

kernels = {
    "filter1": np.array([
    [1, 0, -1],
    [1, 0, -1],
    [1, 0, -1]
], dtype=np.float32),


"filter2": np.array([
    [1, 1, 1],
    [0, 0, 0],
    [-1, -1, -1]
], dtype=np.float32),


"filter3": np.array([
    [1, 0, -1],
    [2, 0, -2],
    [1, 0, -1]
], dtype=np.float32),

"filter4": np.array([
    [1, 2, 1],
    [0, 0, 0],
    [-1, -2, -1]
], dtype=np.float32)

}

for filter_name, kernel in kernels.items():
    filtered_image = cv2.filter2D(original_image, -1, kernel)
    filtered_filename = f'{filter_name}.png'
    cv2.imwrite(filtered_filename, filtered_image)
    print(f"{filtered_filename}")
