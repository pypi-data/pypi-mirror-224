#!/usr/bin/env python3
# encoding=utf-8

import cv2
import argparse


def convert():
    # 设置传入参数
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--src", help="The source image file path.")
    parser.add_argument("-d", "--dst", help="The destination image file path.")
    args = parser.parse_args()

    src_file = args.src
    dst_file = args.dst

    # reading image
    image = cv2.imread(src_file)

    # 先转换为灰图
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    inverted_image = 255 - gray_image
    blurred = cv2.GaussianBlur(inverted_image, (21, 21), 0)
    inverted_blurred = 255 - blurred
    # 输出笔绘图
    pencil_sketch = cv2.divide(gray_image, inverted_blurred, scale=256.0)

    # 保存图片
    cv2.imwrite(dst_file, pencil_sketch)


if __name__ == "__main__":
    convert()
