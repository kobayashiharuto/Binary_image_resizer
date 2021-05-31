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


# 2値画像変換
def convert_binary_image(image):
    image_gray = image.convert('L')
    image_binary = image_gray.point(lambda x: 0 if x < 125 else 255)
    return image_binary


# リサイズ
def resize(image):
    image_resized = image.resize(size=(50, 50))
    return image_resized


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
        image = Image.open(path)
        resized_image = resize(image)
        binary_image = convert_binary_image(resized_image)
        name = path.split('\\')[-1]
        binary_image.save('out/1/' + name)


if __name__ == '__main__':
    main()
