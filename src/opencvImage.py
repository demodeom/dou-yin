import cv2 as cv
import os


def find_bao_xiang(file_name, max_v=0.7):
    current_img = cv.imread(os.getcwd() + '/src/image/current.png')
    bao_xiang = cv.imread(os.getcwd() + '/src/image/' + file_name)
    res = cv.matchTemplate(current_img, bao_xiang, cv.TM_CCOEFF_NORMED)
    _, max_val, _, max_loc = cv.minMaxLoc(res)
    # print(max_val, max_loc)
    h, w = bao_xiang.shape[:-1]
    # print(max_val)
    if max_val >= max_v:
        pos_x = max_loc[0] + w / 2
        pos_y = max_loc[1] + h / 2
        return True, (pos_x, pos_y), max_val
    return False, (0, 0), max_val
