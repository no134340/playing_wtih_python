import numpy as np
from PIL import Image
if __name__ == "__main__":
    image_file = Image.open('watch.jpg')
    image = np.array(image_file)
    pixel = image[0, 0]
    print("Red: {}".format(pixel[0]))
    print("Green: {}".format(pixel[1]))
    print("Blue: {}".format(pixel[2]))
    print(image_file.format, image_file.size, image_file.mode)
    image_file.show()