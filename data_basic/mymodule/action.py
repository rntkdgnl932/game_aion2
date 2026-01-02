import sys
import os
import time
import requests
from PyQt5.QtTest import *
import variable as v_

sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')

import function_game as fg
import traceback
from function_game import click_pos_reg, imgs_set_, click_pos_2


def bag_open(cla):
    import numpy as np
    import cv2
    from jadong import jadong_start
    from clean_screen import clean_screen_start
    print("bag_open")

    try:

        clean_screen_start(cla)

        opened = False
        opened_count = 0

        while opened is False:
            opened_count += 1
            if opened_count > 7:
                opened = True



            full_path = "c:\\my_games\\game_aion2\\data_basic\\imgs\\action\\bag_open\\bag_opened.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(700, 40, 1920, 1040, "one", img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("bag_opened", imgs_)
                full_path = "c:\\my_games\\game_aion2\\data_basic\\imgs\\action\\bag_open\\cube_in.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(700, 40, 1920, 1040, "one", img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("cube_in", imgs_)
                    break
                else:
                    click_pos_reg(1835, 125, cla)
            else:
                click_pos_reg(1715, 75, cla)
            QTest.qWait(1000)
    except Exception as e:
        traceback.print_exc()

def bag_clean_up_start(cla):
    import numpy as np
    import cv2
    from jadong import jadong_start
    from clean_screen import clean_screen_start
    print("bag_clean_up_start")

    try:

        bag_open(cla)

        opened = False
        opened_count = 0

        while opened is False:
            opened_count += 1
            if opened_count > 10:
                opened = True

            full_path = "c:\\my_games\\game_aion2\\data_basic\\imgs\\jadong\\item_clean_up\\choochool_btn.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(900, 700, 1920, 1040, "one", img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("choochool_btn", imgs_)
                confirm_all(cla)
                opened = True
            else:
                full_path = "c:\\my_games\\game_aion2\\data_basic\\imgs\\jadong\\item_clean_up\\choochool.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(1600, 900, 1920, 1040, "one", img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("choochool", imgs_)
                    click_pos_reg(1635, 955, cla)
                    QTest.qWait(1000)
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    QTest.qWait(3000)
                else:
                    full_path = "c:\\my_games\\game_aion2\\data_basic\\imgs\\action\\bag_open\\cube_in.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(700, 40, 1920, 1040, "one", img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("cube_in", imgs_)
                        click_pos_reg(1715, 1015, cla)
            QTest.qWait(1000)
    except Exception as e:
        traceback.print_exc()

def confirm_all(cla):
    import numpy as np
    import cv2
    from jadong import jadong_start
    from clean_screen import clean_screen_start
    print("confirm_all")

    try:

        for i in range(len(v_.confirm_files)):
            full_path = v_.confirm_list + str(
                v_.confirm_files[i])
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(0, 40, 1920, 1040, "one", img, 0.8)
            if imgs_ is not None and imgs_ != False:
                click_pos_reg(imgs_.x, imgs_.y, cla)
                QTest.qWait(500)
    except Exception as e:
        traceback.print_exc()

