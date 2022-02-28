from siamfc import SiamFCTracker
import glob  # glob模块可根据Unix终端所用规则找出所有匹配特定模式的路径名，* ? [] 都可以正确匹配
import os
import cv2
import sys

sys.path.append(os.getcwd())
a = []


def main(videoDir, gpuID, modelPath):
    # sorted() 对所有可迭代的对象进行排序,key是用来比较的元素，取自可迭代对象。
    filenames = sorted(glob.glob(os.path.join(videoDir, "*.jpg")), key=lambda x: int(os.path.basename(x).split('.')[0]))
    print(filenames)


if __name__ == '__main__':
    main('frame', 0, 'models\siamfc_pretrained.pth')
