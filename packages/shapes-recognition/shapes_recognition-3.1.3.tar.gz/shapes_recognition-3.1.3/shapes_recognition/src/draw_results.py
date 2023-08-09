import cv2 as cv

from shapes_recognition.src import cfg
from shapes_recognition.src.create_base import create_base


def draw_self_study_results(
        list_self_study_in, list_self_study_out):

    rows = cfg.n_items
    cols = cfg.n_types

    cfg.show_caption = False
    img_base = create_base(rows, cols)
    create_self_study_in_table(img_base, list_self_study_in)

    cfg.show_caption = True
    img_base = create_base(rows, cols)
    create_self_study_out_table(img_base, list_self_study_out)


def create_self_study_in_table(img_base, list_self_study_in):

    img_table = create_img_table(img_base, list_self_study_in)

    path = cfg.dir_results + '/SELF_STUDY_INPUT.png'

    cv.imwrite(path, img_table)


def create_self_study_out_table(img_base, list_self_study_out):

    img_table = create_img_table(img_base, list_self_study_out)

    path = cfg.dir_results + '/SELF_STUDY_OUTPUT.png'

    cv.imwrite(path, img_table)


def create_img_table(img_base, list_data):

    n_shapes = len(list_data)

    b_list_data = []
    g_list_data = []
    r_list_data = []

    for n in range(n_shapes):

        shape_path = list_data[n]

        shape = cv.imread(shape_path, cv.IMREAD_UNCHANGED)

        if shape.ndim == 2:
            shape = cv.cvtColor(shape, cv.COLOR_GRAY2RGB)

        b_shape, g_shape, r_shape = cv.split(shape)

        b_list_data.append(b_shape)
        g_list_data.append(g_shape)
        r_list_data.append(r_shape)

    b_img_base, g_img_base, r_img_base = cv.split(img_base)

    create_img_table_2(b_img_base, b_list_data)
    create_img_table_2(g_img_base, g_list_data)
    create_img_table_2(r_img_base, r_list_data)

    img_table = cv.merge([b_img_base, g_img_base, r_img_base])

    return img_table


def create_img_table_2(t_img_base, t_list_data):

    rows = cfg.n_items
    cols = cfg.n_types

    n = 0
    for i in range(cols):

        shift_x = i * cfg.cell_width + (i + 1) * cfg.space

        for j in range(rows):
            shift_y = j * cfg.cell_height + cfg.caption_height + j * cfg.space

            t_shape = t_list_data[n]
            n += 1

            add_border_shape(t_shape)

            t_img_base[
                shift_y:cfg.cell_height + shift_y:,
                shift_x:cfg.cell_width + shift_x:] = t_shape[0::, 0::]


def draw_recognition_results(recogn_dictionary):

    rows = cfg.n_items
    cols = cfg.n_types

    cfg.show_caption = True
    img_base = create_base(rows, cols)

    img_table = create_recognition_table(img_base, recogn_dictionary)
    
    path = cfg.dir_results + '/RECOGNITION.png'

    cv.imwrite(path, img_table)


def create_recognition_table(img_base, recogn_dictionary):

    nA = 0
    nB = 0
    nC = 0
    nD = 0

    b_img_base, g_img_base, r_img_base = cv.split(img_base)

    for key, value in recogn_dictionary.items():

        if value == 'A':
            if nA < cfg.n_items:
                shift_x = 0 * cfg.cell_width + 1 * cfg.space
                nA = create_recognition_table_2(
                        shift_x, key, nA,
                        b_img_base, g_img_base, r_img_base)

        if value == 'B':
            if nB < cfg.n_items:
                shift_x = 1 * cfg.cell_width + 2 * cfg.space
                nB = create_recognition_table_2(
                        shift_x, key, nB,
                        b_img_base, g_img_base, r_img_base)

        if value == 'C':
            if nC < cfg.n_items:
                shift_x = 2 * cfg.cell_width + 3 * cfg.space
                nC = create_recognition_table_2(
                        shift_x, key, nC,
                        b_img_base, g_img_base, r_img_base)

        if value == 'D':
            if nD < cfg.n_items:
                shift_x = 3 * cfg.cell_width + 4 * cfg.space
                nD = create_recognition_table_2(
                        shift_x, key, nD,
                        b_img_base, g_img_base, r_img_base)

    img_table = cv.merge([b_img_base, g_img_base, r_img_base])
    
    return img_table


def create_recognition_table_2(
        shift_x, key, n_column,
        b_img_base, g_img_base, r_img_base):

    shift_y = n_column * cfg.cell_height + cfg.caption_height + n_column * cfg.space
    n_column += 1

    shape = cv.imread(key, cv.IMREAD_UNCHANGED)

    if shape.ndim == 2:
        shape = cv.cvtColor(shape, cv.COLOR_GRAY2RGB)

    b_shape, g_shape, r_shape = cv.split(shape)

    add_border_shape(b_shape)
    add_border_shape(g_shape)
    add_border_shape(r_shape)

    b_img_base[
        shift_y:cfg.cell_height + shift_y:,
        shift_x:cfg.cell_width + shift_x:] = b_shape[0::, 0::]
    g_img_base[
        shift_y:cfg.cell_height + shift_y:,
        shift_x:cfg.cell_width + shift_x:] = g_shape[0::, 0::]
    r_img_base[
        shift_y:cfg.cell_height + shift_y:,
        shift_x:cfg.cell_width + shift_x:] = r_shape[0::, 0::]

    return n_column


def add_border_shape(t_shape):

    height = cfg.cell_height
    width = cfg.cell_width

    color = cfg.color_border

    t_shape[0:height, 0] = color
    t_shape[0:height, width - 1] = color
    t_shape[0, 0:width] = color
    t_shape[height - 1, 0:width] = color
