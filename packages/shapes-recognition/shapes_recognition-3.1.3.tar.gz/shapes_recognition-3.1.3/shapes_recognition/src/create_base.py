import cv2 as cv
import numpy as np

from shapes_recognition.src import cfg


def create_base(rows, cols):

    img_base_height = rows * cfg.cell_height + rows * cfg.space + cfg.caption_height
    img_base_width = cols * cfg.cell_width + (cols + 1) * cfg.space

    img_base = np.empty((img_base_height, img_base_width, 3), dtype=np.uint8)
    img_base.fill(cfg.color_background)
    
    img_base = add_caption_and_border(img_base)

    return img_base


def add_caption_and_border(img_base):

    b_img_base, g_img_base, r_img_base = cv.split(img_base)

    if cfg.show_caption:
        font_color = cfg.color_caption_enable
    else:
        font_color = cfg.color_caption_disable

    add_caption(b_img_base, font_color[0])
    add_caption(g_img_base, font_color[1])
    add_caption(r_img_base, font_color[2])

    add_border_img_base(b_img_base)
    add_border_img_base(g_img_base)
    add_border_img_base(r_img_base)

    img_base = cv.merge([b_img_base, g_img_base, r_img_base])

    return img_base


def add_caption(t_img_base, t_font_color):

    x0 = cfg.x_caption_pos + cfg.space
    y0 = cfg.y_caption_pos

    font_scale = cfg.font_scale

    draw_text(t_img_base, x0, y0, font_scale, t_font_color, 'A')
    x0 += cfg.cell_width + cfg.space
    draw_text(t_img_base, x0, y0, font_scale, t_font_color, 'B')
    x0 += cfg.cell_width + cfg.space
    draw_text(t_img_base, x0, y0, font_scale, t_font_color, 'C')
    x0 += cfg.cell_width + cfg.space
    draw_text(t_img_base, x0, y0, font_scale, t_font_color, 'D')


def draw_text(t_img_base, x, y, font_scale, t_font_color, text):
    font = cv.FONT_HERSHEY_SIMPLEX
    thickness = 2
    cv.putText(t_img_base,
               text,
               (x, y),
               font,
               font_scale,
               t_font_color,
               thickness,
               cv.LINE_AA)


def add_border_img_base(t_img_base):

    height = t_img_base.shape[0]
    width = t_img_base.shape[1]

    color = cfg.color_border

    t_img_base[0:height, 0] = color
    t_img_base[0:height, width - 1] = color
    t_img_base[0, 0:width] = color
    t_img_base[height - 1, 0:width] = color
