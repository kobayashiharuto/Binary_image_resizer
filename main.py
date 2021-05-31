import os
import tkinter
import tkinter.messagebox
import tkinter.filedialog
import numpy as np
from PIL import Image
import glob
import matplotlib.pyplot as plt

np.set_printoptions(threshold=10000)


def show_image(image):
    plt.imshow(image)
    plt.show()


def resize(path: str):
    image = Image.open(path)
    image_resized = image.resize(size=(50, 50))
    image_gray = image.convert('L')
    return image_gray


def get_images_from_dir(path: str):
    files = glob.glob(path + '/*')
    return files


def main():
    tkinter.Tk().withdraw()
    directory = tkinter.filedialog.askdirectory(
        initialdir=os.path.abspath(os.path.dirname(__file__)))

    paths = get_images_from_dir(directory)

    for path in paths:
        image = resize(path)
        name = path.split('\\')[-1]
        image.save('out/1/' + name)


if __name__ == '__main__':
    main()
