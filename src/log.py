import os
import time
import random
from shutil import copyfile



def log_warning(img):
    """
    [INFO] [2020-12-02 12:32:12] [未找到] [实时截图: 3423432.png]
    """
    now_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    tmp_png_name = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()) + '.png'

    current_img_path = os.getcwd() + '/src/image/current.png'
    tmp_png_path = os.getcwd() + '/src/log/tmpImg/' + tmp_png_name

    copyfile(current_img_path, tmp_png_path)

    log_info_msg = f"[WARNING] [{now_time}] [{img} 未找到] [实时截图: {tmp_png_name}]"
    log_path = os.getcwd() + '/src/log/'
    log_file_name = time.strftime('%Y-%m-%d', time.localtime()) + '_log.log'
    with open(log_path + log_file_name, 'a') as f:
        f.write(log_info_msg + "\n")
        f.close()
    print(log_info_msg)