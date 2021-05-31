import os
import tkinter
import tkinter.messagebox
import tkinter.filedialog
import numpy as np
from PIL import Image
import glob
import matplotlib.pyplot as plt


def show_image(image):
    plt.imshow(image)
    plt.show()


def convert_binary_image(image):
    image_gray = image.convert('L')
    image_binary = np.array(image_gray, dtype='f')
    resized_image = (image_binary > 100) * 1
    show_image(resized_image)
    return Image.fromarray(resized_image, mode='L')


def resize(path: str):
    image = Image.open(path)
    image_resized = image.resize(size=(50, 50))
    binary_image = convert_binary_image(image_resized)
    show_image(binary_image)
    return binary_image


# ディレクトリから画像パス一覧を取得する
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
