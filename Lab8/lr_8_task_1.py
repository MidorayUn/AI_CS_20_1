# -*- coding: utf-8 -*-
"""LR_8_task_1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1RCYDSihlaBK0wyTnzHv-TRZkw96gaMLh
"""

import cv2
from google.colab.patches import cv2_imshow


# Завантаження та відображення захопленого зображення
img = cv2.imread("Ishchuk.jpg")
cv2_imshow(img)
cv2.waitKey(0)