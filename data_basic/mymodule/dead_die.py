import sys
import os
import time
import requests
from PyQt5.QtTest import *
import variable as v_

sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')

import function_game as fg
import traceback




def dead_check(cla):
    import numpy as np
    import cv2
    import pyautogui
    import random
    from function_game import imgs_set_, click_pos_reg

    print("dead_check")

    try:

        full_path = "c:\\my_games\\game_aion2\\data_basic\\imgs\\check\\dead\\dead_click.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(700, 500, 1000, 900, "one", img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("target_1", imgs_)
            click_pos_reg(imgs_.x, imgs_.y, cla)

    except Exception as e:
        traceback.print_exc()