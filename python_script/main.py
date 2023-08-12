import math
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import cv2

matplotlib.use('TKAgg')

# img = cv2.imread('test2.jpg', cv2.COLOR_BGR2RGB)
img = cv2.imread('test3.jpg')
height, width, channels = img.shape
print(height, width, channels)
print(img.dtype)

tmp = np.zeros((height, width, 3), np.uint8)

p = lambda new, old: (new - old) / old * 100.0
norm = lambda a, b: int(a * b) / b

fx_scale = 2 ** 16
fx_h = (height - 1)
fx_a = norm(math.pi / (height - 1) / 2, fx_scale)

coor = []

for y in range(height):
    theta = math.pi * (y - (height - 1) / 2.0) / (height - 1)
    theta_i = fx_a * (2 * y - fx_h)
    # print(theta, theta_i, p(theta_i, theta))
    for x in range(width):
        #
        phi = (2 * math.pi) * (x - width / 2.0) / width

        phi2 = phi * math.cos(theta)

        # A[x] * B[CST]
        x2 = phi2 * width / (2 * math.pi) + width / 2

        coor.append([y, int(x2)])

        if x2 < 0 or x2 > (width - 1):
            # (B, G, R)
            tmp[y, x] = (0, 0, 255)
        else:
            tmp[y, x] = img[y, int(x2)]

# plt.imshow(img)
print(coor)

tmp = cv2.cvtColor(tmp, cv2.COLOR_BGR2RGB)
# need reordering due to matplot RGB format
plt.imshow(tmp)
plt.show()
