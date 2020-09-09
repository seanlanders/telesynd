#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Binarize (make it black and white) an image with Python."""

from PIL import Image
import numpy


def binarize_image(prefix, img_path, target_path, threshold):
    """Binarize an image."""
    image_file = Image.open(img_path)
    image = image_file.convert('L')  # convert image to monochrome
    image = numpy.array(image)
    image = binarize_array(image, threshold)
    img = Image.fromarray(image.astype(numpy.uint8))
    img.thumbnail((114,96))
    img = img.convert("1")
    img.save(target_path)
    save_cpp(prefix, target_path)
    inoBits = img.tobitmap(prefix)
    print(inoBits)
    return target_path

def save_cpp(prefix, img_path):
    img = Image.open(img_path)
    inoBits = img.tobitmap(prefix)
    target_path = prefix+"-binarize.cpp"
    with open(target_path, "wb") as binary_file:
        binary_file.write(inoBits)
        binary_file.close()
    return target_path

def binarize_array(numpy_array, threshold=200):
    """Binarize a numpy array."""
    for i in range(len(numpy_array)):
        for j in range(len(numpy_array[0])):
            if numpy_array[i][j] > threshold:
                numpy_array[i][j] = 255
            else:
                numpy_array[i][j] = 0
    return numpy_array


def get_parser():
    """Get parser object for script xy.py."""
    from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter
    parser = ArgumentParser(description=__doc__,
                            formatter_class=ArgumentDefaultsHelpFormatter)
    parser.add_argument("-i", "--input",
                        dest="input",
                        help="read this file",
                        metavar="FILE",
                        required=True)
    parser.add_argument("-o", "--output",
                        dest="output",
                        help="write binarized file hre",
                        metavar="FILE",
                        required=True)
    parser.add_argument("--threshold",
                        dest="threshold",
                        default=200,
                        type=int,
                        help="Threshold when to show white")
    return parser


if __name__ == "__main__":
    args = get_parser().parse_args()
    binarize_image(args.input, args.output, args.threshold)