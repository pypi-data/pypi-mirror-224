import sys
import cv2 as cv
import numpy as np

from shapes_recognition.src import cfg
from shapes_recognition.src.check_background import check_background
from shapes_recognition.src.shapes_similarity import shapes_similarity


def get_similarity(path_1, path_2) -> float:

    image, templ = preprocessing(path_1, path_2)

    similarity = shapes_similarity(image, templ)

    return similarity


def preprocessing(path_1, path_2):
    # ---------------------------------------------------------
    shape_1 = cv.imread(str(path_1), cv.IMREAD_GRAYSCALE)
    shape_2 = cv.imread(str(path_2), cv.IMREAD_GRAYSCALE)
    # ---------------------------------------------------------
    height_1 = shape_1.shape[0]
    width_1 = shape_1.shape[1]
    if height_1 != cfg.cell_size or width_1 != cfg.cell_size:
        print(f'\nERROR: ' + path_1 + ' - incorrect size')
        sys.exit(1)

    height_2 = shape_2.shape[0]
    width_2 = shape_2.shape[1]
    if height_2 != cfg.cell_size or width_2 != cfg.cell_size:
        print(f'\nERROR: ' + path_2 + ' - incorrect size')
        sys.exit(1)
    # ---------------------------------------------------------
    shape_1_zoom_out = cv.resize(
        shape_1,
        (cfg.calc_size, cfg.calc_size),
        cv.INTER_LANCZOS4)

    shape_2_zoom_out = cv.resize(
        shape_2,
        (cfg.calc_size, cfg.calc_size),
        cv.INTER_LANCZOS4)
    # ---------------------------------------------------------
    result_1 = check_background(shape_1)
    if result_1 == 0:
        print(f'\nERROR: ' + path_1 + ' - unacceptable shape')
        sys.exit(1)

    result_2 = check_background(shape_2)
    if result_2 == 0:
        print(f'\nERROR: ' + path_2 + ' - unacceptable shape')
        sys.exit(1)
    # ---------------------------------------------------------
    image_invert = np.invert(shape_1_zoom_out)
    templ_invert = np.invert(shape_2_zoom_out)
    # ---------------------------------------------------------
    image_norm = np.zeros((cfg.calc_size, cfg.calc_size), dtype=np.uint8)
    templ_norm = np.zeros((cfg.calc_size, cfg.calc_size), dtype=np.uint8)
    cv.normalize(image_invert, image_norm, 0, 255, cv.NORM_MINMAX)
    cv.normalize(templ_invert, templ_norm, 0, 255, cv.NORM_MINMAX)
    # ---------------------------------------------------------
    return np.uint8(image_norm), np.uint8(templ_norm)
