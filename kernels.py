"""from PIL import Image

image1 = Image.open(r'F:\Chrome Downloads\ITU Internship\lenna.png')
image1.show()
print(image1.size)
"""

import cv2
import numpy as np

original_image = cv2.imread(r'https://www.google.com/imgres?q=lenna&imgurl=https%3A%2F%2Fupload.wikimedia.org%2Fwikipedia%2Fen%2F7%2F7d%2FLenna_%2528test_image%2529.png&imgrefurl=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FLenna&docid=6DW5TB7AAXFPyM&tbnid=3qZwpWtivzR7VM&vet=12ahUKEwiF5tXSg7yNAxVzg_0HHcCwA-gQM3oECBcQAA..i&w=512&h=512&hcb=2&ved=2ahUKEwiF5tXSg7yNAxVzg_0HHcCwA-gQM3oECBcQAA', cv2.IMREAD_GRAYSCALE)

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
