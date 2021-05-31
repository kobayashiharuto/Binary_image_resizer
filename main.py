import os
import tkinter
import tkinter.messagebox
import tkinter.filedialog
import numpy as np
from PIL import Image
import glob


def resize(path: str):
    image = Image.open(path)
    image_resized = image.resize(size=(28, 28))
    image_gray = image_resized.convert('L')
    image_binary = np.array(image_gray, dtype='f')
    resized_image = (image_binary > 20) * 1
    return Image.fromarray(resized_image)


# ディレクトリから画像パス一覧を取得する
def get_images_from_dir(self, path: str):
    files = glob.glob(path + '/*')
    return files


def main():
    tkinter.Tk().withdraw()
    directory = tkinter.filedialog.askdirectory(
        initialdir=os.path.abspath(os.path.dirname(__file__)))

    file_paths = get_images_from_dir(directory)

    images = [resize(path) for path in file_paths]
    


if __name__ == '__main__':
    main()
