import numpy as np

from shapes_recognition.src import cfg


def check_background(any_image: np.uint8) -> int:

    height: int = any_image.shape[0]
    width: int = any_image.shape[1]
    area: int = width * height

    index = np.where(any_image == 255)
    n_white = index[0].size
    part_of_area: float = float(n_white) / float(area)

    if part_of_area < cfg.white_part_param:
        return 0
    else:
        return 1
