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


def clean_screen_start(cla):
    import numpy as np
    import cv2
    from check import out_check
    from action import confirm_all
    print("clean_screen_start")

    try:
        opened = False
        opened_count = 0

        while opened is False:
            opened_count += 1
            if opened_count > 7:
                opened = True

            result_out = out_check(cla)

            if result_out == True:

                opened = True
            else:
                confirm_all(cla)
                close_click(cla)
                skip_click(cla)
            QTest.qWait(1000)
    except Exception as e:
        traceback.print_exc()


def close_click(cla):
    import numpy as np
    import cv2
    from check import out_check
    from function_game import imgs_set_for
    print("close_click")

    try:
        opened = False
        opened_count = 0

        while opened is False:
            opened_count += 1
            if opened_count > 7:
                opened = True

            result_out = out_check(cla)

            if result_out == True:

                opened = True
            else:
                for i in range(len(v_.close_files)):
                    print("list => ", str(v_.close_files[i]))
                    full_path = v_.close_list + str(
                        v_.close_files[i])

                    # ✅ 1) 파일 존재 확인 (없으면 스킵)
                    if not os.path.isfile(full_path):
                        print("[SKIP] file not found:", full_path)
                        continue

                    # ✅ 2) fromfile 실패 방어
                    try:
                        img_array = np.fromfile(full_path, np.uint8)
                    except Exception as e:
                        print("[SKIP] np.fromfile error:", full_path, e)
                        continue

                    # ✅ 3) 빈 파일/읽기 실패 방어
                    if img_array is None or img_array.size == 0:
                        print("[SKIP] empty or unreadable:", full_path)
                        continue

                    # ✅ 4) 디코딩 실패 방어 (img=None 방지)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    if img is None:
                        print("[SKIP] imdecode failed:", full_path)
                        continue

                    imgs_for = imgs_set_for(0, 40, 1920, 1040, "one", img, 0.8)

                    # ✅ 5) imgs_for가 None이면 len()에서 터지므로 순서만 바꿈(구조 유지)
                    if imgs_for is not None and len(imgs_for) > 0:
                        print("close_files", str(v_.close_files[i]), imgs_for)

                        for x in range(len(v_.close_files)):
                            full_path = v_.close_list + str(
                                v_.close_files[x])
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(0, 40, 1920, 1040, "one", img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                QTest.qWait(500)
                    QTest.qWait(100)


            QTest.qWait(500)
    except Exception as e:
        traceback.print_exc()

def skip_click(cla):
    import numpy as np
    import cv2
    from check import out_check
    from function_game import imgs_set_for
    print("skip_click")

    try:
        for x in range(len(v_.skip_files)):
            full_path = v_.skip_list + str(
                v_.skip_files[x])
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(0, 40, 1920, 1040, "one", img, 0.8)
            if imgs_ is not None and imgs_ != False:
                click_pos_reg(imgs_.x, imgs_.y, cla)
                QTest.qWait(500)
    except Exception as e:
        traceback.print_exc()
