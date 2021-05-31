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


def convert_binary_image(image):
    image_gray = image.convert('L')
    image_binary = image_gray.point(lambda x: 0 if x < 125 else 255)
    return image_binary


def resize(path: str):
    image = Image.open(path)
    image_resized = image.resize(size=(50, 50))
    binary_image = convert_binary_image(image_resized)
    show_image(binary_image)
    print(np.asarray(binary_image))
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
