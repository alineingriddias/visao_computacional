import cv2
from matplotlib import pyplot as plt

# def show_image(img, cmap=None):
#     plt.imshow(img, cmap=cmap)
#     plt.axis('off')
#     plt.show()

# image = cv2.imread('exemplo.png')
# image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
# show_image(image_rgb)


image  = cv2.imread('..\exemplo.png')
cv2.imshow('Image', image)
cv2.waitKey(0)

# #converter cor
# cv2.cvtColor(image, conversion)
# #cv2.resize(image,dimension)
# image[point 1 ,point2]  (crop image)

# def convert_color(image, conversion):
#     return cv2.cvtColor(image, conversion)

# def resize_image(image, dimensions):
#     return cv2.resize(image, dimensions)

# def crop_image(image, start_row, start_col, end_row, end_col):
#     return image[start_row:end_row, start_col:end_col]

# def flip_image(image, flip_code):
#     return cv2.flip(image, flip_code)

print("Selecione uma opção: \n1. Converter cor \n2. Redimensionar imagem \n3. Recortar imagem \n4. Espelhar imagem")
option = input("Opção: ")

