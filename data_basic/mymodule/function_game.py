# import random
# import pyautogui
# import pytesseract
# import numpy as np
# import numpy
# from PIL import Image
# import re
# import cv2

from PyQt5.QtTest import *

import time
import sys
import variable as v_

sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')
_SYNC_SER = None
# 파일 최상단 또는 전역 변수 영역
_SHARED_SER = None
def go_test(cla):
    print('hi test!', cla)


def macro_out(cla):
    import os
    try:
        dir_path = "C:\\my_games\\load\\" + str(v_.game_folder)
        file_path = dir_path + "\\start.txt"
        # cla.txt
        cla_data = str(cla) + "cla"
        file_path2 = dir_path + "\\" + cla_data + ".txt"
        with open(file_path, "w", encoding='utf-8-sig') as file:
            data = 'no'
            file.write(str(data))
            time.sleep(0.2)
        with open(file_path2, "w", encoding='utf-8-sig') as file:
            data = cla
            file.write(str(data))
            time.sleep(0.2)
        os.execl(sys.executable, sys.executable, *sys.argv)



    except Exception as e:
        print(e)
        return 0

# 이미지 특정 색상 제외함
def image_processing(src, min_color, max_color):
    import cv2
    import numpy
    try:
        img_ = cv2.cvtColor(numpy.array(src), cv2.COLOR_RGB2BGR)
        exception_img = cv2.inRange(img_, min_color, max_color)
        return exception_img
    except Exception as e:
        print(e)
        return 0


def random_int():
    try:
        import random
        result = random.randint(1, 4)
        return int(result)
    except Exception as e:
        print(e)


def random_int_2():
    try:
        import random
        result = random.randint(100, 200)
        return result
    except Exception as e:
        print(e)


def random_int_3():
    try:
        import random
        result = random.randint(50, 100)
        return result
    except Exception as e:
        print(e)


def isNumber_(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


def change_number_float(many_potion):
    import re
    try:

        potion_ = many_potion

        print("num ??? ", potion_)
        potion_.strip()
        if " " in potion_:
            potion_ = potion_.replace(' ', '')
            print("!!!!!! ['   '] !!!!!!!", potion_)
        # if "\n" in potion_:
        #     potion_ = potion_.replace('\n', '')
        #     print("!!!!!! [' 엔터 제거  '] !!!!!!!", potion_)
        if "고" in potion_:
            potion_ = potion_.replace('고', '2')
            print("!!!!!! [' 고 => 2 '] !!!!!!!", potion_)
        if "ㄷ" in potion_:
            potion_ = potion_.replace('ㄷ', '5')
            print("!!!!!! [' ㄷ => 5 '] !!!!!!!", potion_)
        if "요" in potion_:
            potion_ = potion_.replace('요', '8')
            print("!!!!!! [' 요 => 8 '] !!!!!!!", potion_)
        if "°" in potion_:
            potion_ = potion_.replace('°', '0')
            print("!!!!!! [   ° => 0   ] !!!!!!!", potion_)
        if ")" in potion_:
            potion_ = potion_.replace(')', '1')
            print("!!!!!! [   ) => 1   ] !!!!!!!", potion_)
        if "‘" in potion_:
            potion_ = potion_.replace('‘', '1')
            print("!!!!!! [   ‘ => 1   ] !!!!!!!", potion_)
        if "?" in potion_:
            potion_ = potion_.replace('?', '2')
            print("!!!!!! [   ? => 2  ] !!!!!!!", potion_)
        if "L" in potion_:
            potion_ = potion_.replace('L', '1')
            print("!!!!!! [   L => 1  ] !!!!!!!", potion_)
        if "|" in potion_:
            potion_ = potion_.replace('|', '1')
            print("!!!!!!![   | => 1  ]!!!!!!!!!!!", potion_)
        if "A" in potion_:
            potion_ = potion_.replace('A', '4')
            print("!!!!!!!!![  A => 4 ]!!!!!!!!!!!!!", potion_)
        if "D" in potion_:
            potion_ = potion_.replace('D', '2')
            print("!!!!!!!!![  D => 2 ]!!!!!!!!!!!!!", potion_)
        if "G" in potion_:
            potion_ = potion_.replace('G', '6')
            print("!!!!!!!!![  G => 6 ]!!!!!!!!!!!!!", potion_)
        if "B" in potion_:
            potion_ = potion_.replace('B', '8')
            print("!!!!!!!!![  B => 8  ]!!!!!!!!!!!!!", potion_)
        if "T" in potion_:
            potion_ = potion_.replace('T', '7')
            print("!!!!!!!!![  T => 7  ]!!!!!!!!!!!!!", potion_)
        if "S" in potion_:
            potion_ = potion_.replace('S', '5')
            print("!!!!!!!!![  S => 5  ]!!!!!!!!!!!!!", potion_)
        if "Q" in potion_:
            potion_ = potion_.replace('Q', '9')
            print("!!!!!!!!![  Q => 9  ]!!!!!!!!!!!!!", potion_)
        if "F" in potion_:
            potion_ = potion_.replace('F', '9')
            print("!!!!!!!!![  F => 9  ]!!!!!!!!!!!!!", potion_)
        if "R" in potion_:
            potion_ = potion_.replace('R', '8')
            print("!!!!!!!!![  R => 8  ]!!!!!!!!!!!!!", potion_)
        if "a" in potion_:
            potion_ = potion_.replace('a', '4')
            print("!!!!!!!!![  a => 4  ]!!!!!!!!!!!!!", potion_)
        if "g" in potion_:
            potion_ = potion_.replace('g', '9')
            print("!!!!!!!!![  g => 9  ]!!!!!!!!!!!!!", potion_)
        if "i" in potion_:
            potion_ = potion_.replace('i', '1')
            print("!!!!!!!!![  i => 1  ]!!!!!!!!!!!!!", potion_)
        if "l" in potion_:
            potion_ = potion_.replace('l', '1')
            print("!!!!!!!!![  l => 1  ]!!!!!!!!!!!!!", potion_)
        if "u" in potion_:
            potion_ = potion_.replace('u', '11')
            print("!!!!!!!!![  u => 11  ]!!!!!!!!!!!!!", potion_)
        if "s" in potion_:
            potion_ = potion_.replace('s', '5')
            print("!!!!!!!!![  s => 5  ]!!!!!!!!!!!!!", potion_)

        potion_ = potion_.replace(',', '').strip()
        potion_ = float(potion_)

        return potion_
    except Exception as e:
        print(e)


def change_number(many_potion):
    try:

        potion_ = many_potion

        for i in range(5):
            print("i", i)
            print("num ??? ", potion_)
            result_digit = potion_.isdigit()

            if result_digit == True:
                break
            else:
                if " " in potion_:
                    potion_ = potion_.replace(' ', '')
                    print("!!!!!! ['   '] !!!!!!!", potion_)
                if "고" in potion_:
                    potion_ = potion_.replace('고', '2')
                    print("!!!!!! [' 고 => 2 '] !!!!!!!", potion_)
                if "ㄷ" in potion_:
                    potion_ = potion_.replace('ㄷ', '5')
                    print("!!!!!! [' ㄷ => 5 '] !!!!!!!", potion_)
                if "요" in potion_:
                    potion_ = potion_.replace('요', '8')
                    print("!!!!!! [' 요 => 8 '] !!!!!!!", potion_)
                if "°" in potion_:
                    potion_ = potion_.replace('°', '0')
                    print("!!!!!! [   ° => 0   ] !!!!!!!", potion_)
                if ")" in potion_:
                    potion_ = potion_.replace(')', '1')
                    print("!!!!!! [   ) => 1   ] !!!!!!!", potion_)
                if "‘" in potion_:
                    potion_ = potion_.replace('‘', '1')
                    print("!!!!!! [   ‘ => 1   ] !!!!!!!", potion_)
                if "?" in potion_:
                    potion_ = potion_.replace('?', '2')
                    print("!!!!!! [   ? => 2  ] !!!!!!!", potion_)
                if "L" in potion_:
                    potion_ = potion_.replace('L', '1')
                    print("!!!!!! [   L => 1  ] !!!!!!!", potion_)
                if "|" in potion_:
                    potion_ = potion_.replace('|', '1')
                    print("!!!!!!![   | => 1  ]!!!!!!!!!!!", potion_)
                if "A" in potion_:
                    potion_ = potion_.replace('A', '4')
                    print("!!!!!!!!![  A => 4 ]!!!!!!!!!!!!!", potion_)
                if "D" in potion_:
                    potion_ = potion_.replace('D', '2')
                    print("!!!!!!!!![  D => 2 ]!!!!!!!!!!!!!", potion_)
                if "G" in potion_:
                    potion_ = potion_.replace('G', '6')
                    print("!!!!!!!!![  G => 6 ]!!!!!!!!!!!!!", potion_)
                if "B" in potion_:
                    potion_ = potion_.replace('B', '8')
                    print("!!!!!!!!![  B => 8  ]!!!!!!!!!!!!!", potion_)
                if "T" in potion_:
                    potion_ = potion_.replace('T', '7')
                    print("!!!!!!!!![  T => 7  ]!!!!!!!!!!!!!", potion_)
                if "S" in potion_:
                    potion_ = potion_.replace('S', '5')
                    print("!!!!!!!!![  S => 5  ]!!!!!!!!!!!!!", potion_)
                if "Q" in potion_:
                    potion_ = potion_.replace('Q', '9')
                    print("!!!!!!!!![  Q => 9  ]!!!!!!!!!!!!!", potion_)
                if "F" in potion_:
                    potion_ = potion_.replace('F', '9')
                    print("!!!!!!!!![  F => 9  ]!!!!!!!!!!!!!", potion_)
                if "R" in potion_:
                    potion_ = potion_.replace('R', '8')
                    print("!!!!!!!!![  R => 8  ]!!!!!!!!!!!!!", potion_)
                if "a" in potion_:
                    potion_ = potion_.replace('a', '4')
                    print("!!!!!!!!![  a => 4  ]!!!!!!!!!!!!!", potion_)
                if "g" in potion_:
                    potion_ = potion_.replace('g', '9')
                    print("!!!!!!!!![  g => 9  ]!!!!!!!!!!!!!", potion_)
                if "u" in potion_:
                    potion_ = potion_.replace('u', '11')
                    print("!!!!!!!!![  u => 11  ]!!!!!!!!!!!!!", potion_)
                if "s" in potion_:
                    potion_ = potion_.replace('s', '5')
                    print("!!!!!!!!![  s => 5  ]!!!!!!!!!!!!!", potion_)

        potion_ = int_put_(potion_)

        if potion_[0] == "0":
            potion_ = "1" + potion_
            print("potion_ = '1' + potion_", potion_)

        return potion_
    except Exception as e:
        print(e)


def int_put_(data):
    try:
        import re
        data_ = data.replace(',', '').strip()
        data_2 = data_.replace('.', '').strip()
        data_3 = data_2.replace(' ', '').strip()
        data_4 = data_3.replace('/', '').strip()

        # data_2 = data_.strip().replace('.', '')
        # data_3 = data_2.strip().replace(' ', '')
        # data_4 = data_3.strip().replace('/', '')
        result = re.sub(r'[^0-9]', '', data_4)
        return result
    except ValueError:
        return False


def float_put_(data):
    try:
        import re
        data_ = data.replace(',', '').strip()
        data_2 = data_.replace('.', '').strip()
        data_3 = data_2.replace(' ', '').strip()
        data_4 = data_3.replace('/', '').strip()

        # data_2 = data_.strip().replace('.', '')
        # data_3 = data_2.strip().replace(' ', '')
        # data_4 = data_3.strip().replace('/', '')
        result = re.sub(r'[^0-9]', '', data_4)
        return result
    except ValueError:
        return False


def in_number_check(data):
    import cv2
    import numpy as np
    try:

        isNumber = False
        # print("들어온 데이타?", data)
        # print("len potion", len(data))
        if len(data) > 0:
            # print("길이가 0 보다 크다", len(data))
            for i in range(len(data)):
                result_num_bool = data[i].isdigit()
                if result_num_bool == True:
                    isNumber = True
        else:
            print("데이터가 길이가 없고 비어있다")

        return isNumber
    except Exception as e:
        print(e)


def imgs_set(a, b, c, d, cla, img):
    try:
        from PIL import ImageGrab
        from functools import partial
        import pyautogui

        ImageGrab.grab = partial(ImageGrab.grab, all_screens=True)

        if cla == 'one':
            plus = 0
        if cla == 'two':
            plus = 960
        if cla == 'three':
            plus = 960 * 2
        if cla == 'four':
            plus = 960 * 3
        if cla == 'five':
            plus = 960 * 4
        if cla == 'six':
            plus = 960 * 5

        result = pyautogui.locateCenterOnScreen(img, region=(a + plus, b, c - a + 10, d - b + 10),
                                                confidence=0.7)
        return result
    except ValueError:
        return False


def imgs_set_(a, b, c, d, cla, img, data):
    try:
        from PIL import ImageGrab
        from functools import partial
        import pyautogui

        # pyautogui가 "못찾음"을 예외로 던지는 버전이 있음.
        # 이 플래그를 False로 하면 None 반환 쪽으로 동작하는 경우가 많음.
        try:
            pyautogui.USE_IMAGE_NOT_FOUND_EXCEPTION = False
        except Exception:
            pass

        ImageGrab.grab = partial(ImageGrab.grab, all_screens=True)

        if cla == 'one':
            plus = 0
        if cla == 'two':
            plus = 960
        if cla == 'three':
            plus = 960 * 2
        if cla == 'four':
            plus = 960 * 3
        if cla == 'five':
            plus = 960 * 4
        if cla == 'six':
            plus = 960 * 5

        # 못 찾으면 예외가 아니라 None으로 처리해야 자동 루프가 계속 돈다.
        try:
            result = pyautogui.locateCenterOnScreen(
                img,
                region=(a + plus, b, c - a, d - b),
                confidence=data
            )
            return result  # 찾으면 (x,y), 못 찾으면 None
        except Exception:
            # ImageNotFoundException / pyautogui.ImageNotFoundException 등
            return None

    except Exception:
        return False


def imgs_set_num(a, b, c, d, cla, img, data):
    try:
        from PIL import ImageGrab
        from functools import partial
        import pyautogui

        ImageGrab.grab = partial(ImageGrab.grab, all_screens=True)

        if cla == 'one':
            plus = 0
        if cla == 'two':
            plus = 960
        if cla == 'three':
            plus = 960 * 2
        if cla == 'four':
            plus = 960 * 3
        if cla == 'five':
            plus = 960 * 4
        if cla == 'six':
            plus = 960 * 5

        # pos = (a + plus, b, c - a, d - b)
        # pyautogui.screenshot("asd.png", region=pos)

        result = pyautogui.locateCenterOnScreen(img, region=(a + plus, b, c - a, d - b),
                                                confidence=data)
        return result
    except ValueError:
        return False


def imgs_set_reg(a, b, c, d, cla, img, data):
    try:
        from PIL import ImageGrab
        from functools import partial
        import pyautogui

        ImageGrab.grab = partial(ImageGrab.grab, all_screens=True)

        if cla == 'one':
            plus = 0
        if cla == 'two':
            plus = 0
        if cla == 'three':
            plus = 0
        if cla == 'four':
            plus = 0
        if cla == 'five':
            plus = 0
        if cla == 'six':
            plus = 0

        # pos = (a + plus, b, c - a, d - b)
        # pyautogui.screenshot("asd.png", region=pos)

        result = pyautogui.locateCenterOnScreen(img, region=(a + plus, b, c - a, d - b),
                                                confidence=data)
        return result
    except ValueError:
        return False


def imgs_set_for(a, b, c, d, cla, img, data):
    try:
        from PIL import ImageGrab
        from functools import partial
        import pyautogui

        ImageGrab.grab = partial(ImageGrab.grab, all_screens=True)

        # 예시
        # full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\jadong\\bookmark_star.PNG"
        # img_array = np.fromfile(full_path, np.uint8)
        # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        # imgs_ = imgs_set_for(870, 420, 950, 720, cla, img, 0.85)
        # if imgs_ is not None and imgs_ != False:
        #     print("bookmark_star", imgs_)
        #     for i in range(len(imgs_)):
        #         print("imgs_", i, imgs_[i])
        #         print("imgs_", i, imgs_[i][0])
        #         print("imgs_", i, imgs_[i][1])

        if cla == 'one':
            plus = 0
        if cla == 'two':
            plus = 960
        if cla == 'three':
            plus = 960 * 2
        if cla == 'four':
            plus = 960 * 3
        if cla == 'five':
            plus = 960 * 4
        if cla == 'six':
            plus = 960 * 5
        try:
            regs = []

            for i in pyautogui.locateAllOnScreen(img, region=(a + plus, b, c - a, d - b), confidence=data):
                print('i', i)
                last_x = i.left + int(i.width / 2)
                last_y = i.top + int(i.height / 2)
                last = [last_x, last_y]
                regs.append(last)

            return regs
        except Exception:
            return None
    except ValueError:
        return False


def click_with_image(image_path):
    try:
        from PIL import ImageGrab
        from functools import partial
        import pyautogui

        ImageGrab.grab = partial(ImageGrab.grab, all_screens=True)

        isClick = False
        data_count = 0
        while isClick is False:
            data_count += 1
            if data_count > 7:
                isClick = True
            location = pyautogui.locateOnScreen(image_path)
            if location is not None:
                pyautogui.click(location)
                isClick = True
    except Exception as e:
        print(e)


def get_region(start_x, start_y, end_x, end_y, cla):
    coordinate = 0
    if cla == 'one':
        coordinate = 0
    if cla == 'two':
        coordinate = 960
    if cla == 'three':
        coordinate = 960 * 2
    if cla == 'four':
        coordinate = 960 * 3
    if cla == 'five':
        coordinate = 960 * 4
    if cla == 'six':
        coordinate = 960 * 5

    value = (start_x + coordinate, start_y, end_x - start_x, end_y - start_y)
    return value


def click_pos(pos):
    try:
        import pyautogui
        pyautogui.moveTo(pos[0] + random_int(), pos[1] + random_int())
        time.sleep(random_int())
        pyautogui.click()
    except Exception as e:
        print(e)


def mouse_move(x, y):
    import pydirectinput
    try:
        reg_x = x + random_int()
        reg_y = y + random_int()
        pydirectinput.moveTo(reg_x, reg_y)
        print("mouse_move", reg_x, reg_y)

    except Exception as e:
        print(e)
        return 0


def win_left_move(cla):
    try:
        import serial

        arduino_port = v_.COM_
        baudrate = v_.speed_

        print("win_left_move", cla)

        ser = serial.Serial(arduino_port, baudrate)

        moveX = 0
        moveY = 0
        moveZ = 7

        data = f'x = {moveX}, y = {moveY}, z = {moveZ}\n'
        ser.write(data.encode())

        ser.close()
        QTest.qWait(10)

    except Exception as e:
        print(e)
        return 0


def win_right_move(cla):
    try:
        import serial

        arduino_port = v_.COM_
        baudrate = v_.speed_

        print("win_right_move", cla)

        ser = serial.Serial(arduino_port, baudrate)

        moveX = 0
        moveY = 0
        moveZ = 6

        data = f'x = {moveX}, y = {moveY}, z = {moveZ}\n'
        ser.write(data.encode())

        ser.close()
        QTest.qWait(10)

    except Exception as e:
        print(e)
        return 0


def click_pos_2(pos_1, pos_2, cla):
    try:
        import serial
        import pyautogui

        pos_1 = int(pos_1)
        pos_2 = int(pos_2)

        coordinate = 0
        if cla == 'one':
            coordinate = 0
        if cla == 'two':
            coordinate = 960
        if cla == 'three':
            coordinate = 960 * 2
        if cla == 'four':
            coordinate = 960 * 3
        if cla == 'five':
            coordinate = 960 * 4
        if cla == 'six':
            coordinate = 960 * 5

        pyautogui.moveTo(pos_1 + coordinate, pos_2)

        if v_.now_arduino == "on":
            arduino_port = v_.COM_
            baudrate = v_.speed_

            ser = serial.Serial(arduino_port, baudrate)

            moveZ = 1
            k_reg = v_.mouse_speed
            c_reg = v_.mouse_pm

            move_ = False
            move_count = 0
            while move_ is False:
                move_count += 1
                if move_count > v_.mouse_move_count:
                    print("move_count", move_count)
                    move_ = True

                # 이동 시킬 포인트 계산
                x_reg = pos_1 + coordinate - pyautogui.position()[0]
                y_reg = pos_2 - pyautogui.position()[1]
                # if move_count > 280:
                #     print("이동 시킬 포인트 계산 y_reg", y_reg)

                if -c_reg < x_reg < c_reg:
                    moveX = x_reg
                elif x_reg > 0:
                    if x_reg == k_reg:
                        moveX = x_reg
                    else:
                        moveX = min(k_reg, x_reg)
                else:
                    if x_reg == -k_reg:
                        moveX = x_reg
                    else:
                        moveX = max(-k_reg, x_reg)

                if -c_reg < y_reg < c_reg:
                    moveY = y_reg
                elif y_reg > 0:
                    if y_reg == k_reg:
                        moveY = y_reg
                    else:
                        moveY = min(k_reg, y_reg)
                else:
                    if y_reg == -k_reg:
                        moveY = y_reg
                    else:
                        moveY = max(-k_reg, y_reg)

                # # 이동 시킬 포인트 결과값
                # print("이동 시킬 포인트 결과값 moveY", moveY)

                data = f'x = {moveX}, y = {moveY}, z = {moveZ}\n'
                ser.write(data.encode())
                received_data = ser.readline().decode().strip()

                if -c_reg < moveX < c_reg and -c_reg < moveY < c_reg:
                    x_reg = pos_1 + coordinate - pyautogui.position()[0]
                    y_reg = pos_2 - pyautogui.position()[1]
                    if -c_reg < x_reg < c_reg and -c_reg < y_reg < c_reg and pyautogui.position()[1] >= 31:
                        # print("move_count", move_count)
                        # print("moveX", moveX)
                        # print("moveY", moveY)
                        # print("x_reg", x_reg)
                        # print("y_reg", y_reg)
                        move_ = True

                        # moveZ = 2
                        # data = f'x = {moveX}, y = {moveY}, z = {moveZ}\n'
                        # ser.write(data.encode())

                        moveX = 0
                        moveY = 0
                        moveZ = 3
                        data = f'x = {moveX}, y = {moveY}, z = {moveZ}\n'
                        ser.write(data.encode())

                        time.sleep(0.1)

                        moveX = 0
                        moveY = 0
                        moveZ = 4
                        data = f'x = {moveX}, y = {moveY}, z = {moveZ}\n'
                        ser.write(data.encode())

                # else:
                #     print("아직 오차 범위 밖이다...", move_count)
                #     print("x_reg", x_reg)
                #     print("y_reg", y_reg)
            ser.close()
            QTest.qWait(10)
        else:

            # pyautogui.moveTo(pos_1 + random_int() + coordinate, pos_2 + random_int())
            # time.sleep(0.2)
            pyautogui.click(pos_1 + random_int() + coordinate, pos_2 + random_int())
        time.sleep(0.1)

    except Exception as e:
        print("error:", e)





def mouse_down_abs(pos_1, pos_2, cla):
    """지정한 절대 좌표에서 마우스 왼쪽 버튼을 누른 상태로 유지"""
    import serial
    import pyautogui
    try:
        pos_1, pos_2 = int(pos_1), int(pos_2)
        pyautogui.moveTo(pos_1, pos_2) # 해당 위치로 이동

        if v_.now_arduino == "on":
            # 아두이노 모드: MD L (Mouse Down Left) 명령 전송
            arduino_mousedown_left() # 기존 작성된 함수 활용
        else:
            # 일반 모드: pyautogui 활용
            pyautogui.mouseDown(pos_1, pos_2, button='left')
    except Exception as e:
        print(f"mouse_down_abs Error: {e}")

def mouse_up_abs(pos_1, pos_2, cla):
    """마우스 왼쪽 버튼을 뗌"""
    import serial
    import pyautogui
    try:
        if v_.now_arduino == "on":
            # 아두이노 모드: MU L (Mouse Up Left) 명령 전송
            arduino_mouseup_left() # 기존 작성된 함수 활용
        else:
            pyautogui.mouseUp(button='left')
    except Exception as e:
        print(f"mouse_up_abs Error: {e}")

def click_pos_reg(pos_1, pos_2, cla):
    import serial
    import pyautogui
    try:

        pos_1 = int(pos_1)
        pos_2 = int(pos_2)

        coordinate = 0
        if cla == 'one':
            coordinate = 0
        if cla == 'two':
            coordinate = 0
        if cla == 'three':
            coordinate = 0
        if cla == 'four':
            coordinate = 0
        if cla == 'five':
            coordinate = 0
        if cla == 'six':
            coordinate = 0

        pyautogui.moveTo(pos_1 + coordinate, pos_2)

        if v_.now_arduino == "on":
            arduino_port = v_.COM_
            baudrate = v_.speed_

            ser = serial.Serial(arduino_port, baudrate)

            moveZ = 1
            k_reg = v_.mouse_speed
            c_reg = v_.mouse_pm

            move_ = False
            move_count = 0
            while move_ is False:
                move_count += 1
                if move_count > v_.mouse_move_count:
                    move_ = True

                # 이동 시킬 포인트 계산
                x_reg = pos_1 + coordinate - pyautogui.position()[0]
                y_reg = pos_2 - pyautogui.position()[1]

                if -c_reg < x_reg < c_reg:
                    moveX = x_reg
                elif x_reg > 0:
                    if x_reg == k_reg:
                        moveX = x_reg
                    else:
                        moveX = min(k_reg, x_reg)
                else:
                    if x_reg == -k_reg:
                        moveX = x_reg
                    else:
                        moveX = max(-k_reg, x_reg)

                if -c_reg < y_reg < c_reg:
                    moveY = y_reg
                elif y_reg > 0:
                    if y_reg == k_reg:
                        moveY = y_reg
                    else:
                        moveY = min(k_reg, y_reg)
                else:
                    if y_reg == -k_reg:
                        moveY = y_reg
                    else:
                        moveY = max(-k_reg, y_reg)

                data = f'x = {moveX}, y = {moveY}, z = {moveZ}\n'
                ser.write(data.encode())
                received_data = ser.readline().decode().strip()

                if received_data == '0' or (-c_reg < moveX < c_reg and -c_reg < moveY < c_reg):
                    x_reg = pos_1 + coordinate - pyautogui.position()[0]
                    y_reg = pos_2 - pyautogui.position()[1]
                    if -c_reg < x_reg < c_reg and -c_reg < y_reg < c_reg and pyautogui.position()[1] >= 31:
                        move_ = True

                        # moveZ = 2
                        # data = f'x = {moveX}, y = {moveY}, z = {moveZ}\n'
                        # ser.write(data.encode())

                        moveX = 0
                        moveY = 0
                        moveZ = 3
                        data = f'x = {moveX}, y = {moveY}, z = {moveZ}\n'
                        ser.write(data.encode())

                        time.sleep(0.1)

                        moveX = 0
                        moveY = 0
                        moveZ = 4
                        data = f'x = {moveX}, y = {moveY}, z = {moveZ}\n'
                        ser.write(data.encode())

                        # drag_pos_Press()
                        # time.sleep(0.1)
                        # drag_pos_Release()

            ser.close()
            QTest.qWait(10)
        else:

            # pyautogui.moveTo(pos_1 + random_int() + coordinate, pos_2 + random_int())

            pyautogui.click(pos_1 + random_int() + coordinate, pos_2 + random_int())
        time.sleep(0.1)


    except Exception as e:
        print("error:", e)


def mouse_move_cpp(pos_1, pos_2, cla):
    try:
        import serial
        import pyautogui

        pos_1 = int(pos_1)
        pos_2 = int(pos_2)

        arduino_port = v_.COM_
        baudrate = v_.speed_

        coordinate = 0
        if cla == 'one':
            coordinate = 0
        if cla == 'two':
            coordinate = 960
        if cla == 'three':
            coordinate = 960 * 2
        if cla == 'four':
            coordinate = 960 * 3
        if cla == 'five':
            coordinate = 960 * 4
        if cla == 'six':
            coordinate = 960 * 5

        pyautogui.moveTo(pos_1 + coordinate, pos_2)

        if v_.now_arduino == "on":

            ser = serial.Serial(arduino_port, baudrate)

            moveZ = 1
            k_reg = v_.mouse_speed
            c_reg = v_.mouse_pm

            move_ = False
            move_count = 0
            while move_ is False:
                move_count += 1
                if move_count > v_.mouse_move_count:
                    move_ = True

                # 이동 시킬 포인트 계산
                x_reg = pos_1 + coordinate - pyautogui.position()[0]
                y_reg = pos_2 - pyautogui.position()[1]

                if -c_reg < x_reg < c_reg:
                    moveX = x_reg
                elif x_reg > 0:
                    if x_reg == k_reg:
                        moveX = x_reg
                    else:
                        moveX = min(k_reg, x_reg)
                else:
                    if x_reg == -k_reg:
                        moveX = x_reg
                    else:
                        moveX = max(-k_reg, x_reg)

                if -c_reg < y_reg < c_reg:
                    moveY = y_reg
                elif y_reg > 0:
                    if y_reg == k_reg:
                        moveY = y_reg
                    else:
                        moveY = min(k_reg, y_reg)
                else:
                    if y_reg == -k_reg:
                        moveY = y_reg
                    else:
                        moveY = max(-k_reg, y_reg)

                data = f'x = {moveX}, y = {moveY}, z = {moveZ}\n'
                ser.write(data.encode())
                received_data = ser.readline().decode().strip()

                if -c_reg < moveX < c_reg and -c_reg < moveY < c_reg:
                    x_reg = pos_1 + coordinate - pyautogui.position()[0]
                    y_reg = pos_2 - pyautogui.position()[1]
                    if -c_reg < x_reg < c_reg and -c_reg < y_reg < c_reg and pyautogui.position()[1] >= 31:
                        move_ = True
                        data = f'x = {moveX}, y = {moveY}, z = {moveZ}\n'
                        ser.write(data.encode())

            ser.close()
            QTest.qWait(10)
        else:
            pyautogui.moveTo(pos_1 + random_int() + coordinate, pos_2 + random_int(), 0.1)

    except Exception as e:
        print("error:", e)


def mouse_move_cpp_reg(pos_1, pos_2, cla):
    try:
        import serial
        import pyautogui

        pos_1 = int(pos_1)
        pos_2 = int(pos_2)

        arduino_port = v_.COM_
        baudrate = v_.speed_

        coordinate = 0

        # pyautogui.moveTo(pos_1 + coordinate, pos_2)

        if v_.now_arduino == "on":

            ser = serial.Serial(arduino_port, baudrate)

            moveZ = 1
            k_reg = v_.mouse_speed
            c_reg = v_.mouse_pm

            move_ = False
            move_count = 0
            while move_ is False:
                move_count += 1
                if move_count > v_.mouse_move_count:
                    move_ = True

                # 이동 시킬 포인트 계산
                x_reg = pos_1 + coordinate - pyautogui.position()[0]
                y_reg = pos_2 - pyautogui.position()[1]

                if -c_reg < x_reg < c_reg:
                    moveX = x_reg
                elif x_reg > 0:
                    if x_reg == k_reg:
                        moveX = x_reg
                    else:
                        moveX = min(k_reg, x_reg)
                else:
                    if x_reg == -k_reg:
                        moveX = x_reg
                    else:
                        moveX = max(-k_reg, x_reg)

                if -c_reg < y_reg < c_reg:
                    moveY = y_reg
                elif y_reg > 0:
                    if y_reg == k_reg:
                        moveY = y_reg
                    else:
                        moveY = min(k_reg, y_reg)
                else:
                    if y_reg == -k_reg:
                        moveY = y_reg
                    else:
                        moveY = max(-k_reg, y_reg)

                data = f'x = {moveX}, y = {moveY}, z = {moveZ}\n'
                ser.write(data.encode())
                received_data = ser.readline().decode().strip()

                if -c_reg < moveX < c_reg and -c_reg < moveY < c_reg:
                    x_reg = pos_1 + coordinate - pyautogui.position()[0]
                    y_reg = pos_2 - pyautogui.position()[1]
                    if -c_reg < x_reg < c_reg and -c_reg < y_reg < c_reg and pyautogui.position()[1] >= 31:
                        move_ = True
                        data = f'x = {moveX}, y = {moveY}, z = {moveZ}\n'
                        ser.write(data.encode())

            ser.close()
            QTest.qWait(10)
        else:
            pyautogui.moveTo(pos_1 + random_int() + coordinate, pos_2 + random_int(), 0.1)

    except Exception as e:
        print("error:", e)


def mouse_move_drag(pos_1, pos_2, cla, speed):
    try:
        import serial
        import pyautogui

        pos_1 = int(pos_1)
        pos_2 = int(pos_2)

        arduino_port = v_.COM_
        baudrate = v_.speed_

        coordinate = 0
        if cla == 'one':
            coordinate = 0
        if cla == 'two':
            coordinate = 960
        if cla == 'three':
            coordinate = 960 * 2
        if cla == 'four':
            coordinate = 960 * 3
        if cla == 'five':
            coordinate = 960 * 4
        if cla == 'six':
            coordinate = 960 * 5

        if v_.now_arduino == "on":

            ser = serial.Serial(arduino_port, baudrate)

            moveZ = 1
            k_reg = speed
            c_reg = v_.mouse_pm

            move_ = False
            move_count = 0
            while move_ is False:
                move_count += 1
                if move_count > v_.mouse_move_count:
                    move_ = True

                # 이동 시킬 포인트 계산
                x_reg = pos_1 + coordinate - pyautogui.position()[0]
                y_reg = pos_2 - pyautogui.position()[1]

                if -c_reg < x_reg < c_reg:
                    moveX = x_reg
                elif x_reg > 0:
                    if x_reg == k_reg:
                        moveX = x_reg
                    else:
                        moveX = min(k_reg, x_reg)
                else:
                    if x_reg == -k_reg:
                        moveX = x_reg
                    else:
                        moveX = max(-k_reg, x_reg)

                if -c_reg < y_reg < c_reg:
                    moveY = y_reg
                elif y_reg > 0:
                    if y_reg == k_reg:
                        moveY = y_reg
                    else:
                        moveY = min(k_reg, y_reg)
                else:
                    if y_reg == -k_reg:
                        moveY = y_reg
                    else:
                        moveY = max(-k_reg, y_reg)

                data = f'x = {moveX}, y = {moveY}, z = {moveZ}\n'
                ser.write(data.encode())
                received_data = ser.readline().decode().strip()

                if -c_reg < moveX < c_reg and -c_reg < moveY < c_reg:
                    x_reg = pos_1 + coordinate - pyautogui.position()[0]
                    y_reg = pos_2 - pyautogui.position()[1]
                    if -c_reg < x_reg < c_reg and -c_reg < y_reg < c_reg and pyautogui.position()[1] >= 31:
                        move_ = True
                        data = f'x = {moveX}, y = {moveY}, z = {moveZ}\n'
                        ser.write(data.encode())

            ser.close()
            QTest.qWait(10)
        else:
            pyautogui.moveTo(pos_1 + random_int() + coordinate, pos_2 + random_int(), 0.1)

    except Exception as e:
        print("error:", e)


def mouse_move_drag_reg(pos_1, pos_2, cla, speed):
    try:
        import serial
        import pyautogui

        pos_1 = int(pos_1)
        pos_2 = int(pos_2)

        arduino_port = v_.COM_
        baudrate = v_.speed_

        coordinate = 0

        if v_.now_arduino == "on":

            ser = serial.Serial(arduino_port, baudrate)

            moveZ = 1
            k_reg = speed
            c_reg = v_.mouse_pm

            move_ = False
            move_count = 0
            while move_ is False:
                move_count += 1
                if move_count > v_.mouse_move_count:
                    move_ = True

                # 이동 시킬 포인트 계산
                x_reg = pos_1 + coordinate - pyautogui.position()[0]
                y_reg = pos_2 - pyautogui.position()[1]

                if -c_reg < x_reg < c_reg:
                    moveX = x_reg
                elif x_reg > 0:
                    if x_reg == k_reg:
                        moveX = x_reg
                    else:
                        moveX = min(k_reg, x_reg)
                else:
                    if x_reg == -k_reg:
                        moveX = x_reg
                    else:
                        moveX = max(-k_reg, x_reg)

                if -c_reg < y_reg < c_reg:
                    moveY = y_reg
                elif y_reg > 0:
                    if y_reg == k_reg:
                        moveY = y_reg
                    else:
                        moveY = min(k_reg, y_reg)
                else:
                    if y_reg == -k_reg:
                        moveY = y_reg
                    else:
                        moveY = max(-k_reg, y_reg)

                data = f'x = {moveX}, y = {moveY}, z = {moveZ}\n'
                ser.write(data.encode())
                received_data = ser.readline().decode().strip()

                if -c_reg < moveX < c_reg and -c_reg < moveY < c_reg:
                    x_reg = pos_1 + coordinate - pyautogui.position()[0]
                    y_reg = pos_2 - pyautogui.position()[1]
                    if -c_reg < x_reg < c_reg and -c_reg < y_reg < c_reg and pyautogui.position()[1] >= 31:
                        move_ = True
                        data = f'x = {moveX}, y = {moveY}, z = {moveZ}\n'
                        ser.write(data.encode())

            ser.close()
            QTest.qWait(10)


        else:
            pyautogui.moveTo(pos_1 + random_int() + coordinate, pos_2 + random_int(), 0.1)

    except Exception as e:
        print("error:", e)


def mouse_move_adu_drag(pos_1, pos_2, cla):
    try:
        import serial
        import pyautogui

        pos_1 = int(pos_1)
        pos_2 = int(pos_2)

        arduino_port = v_.COM_
        baudrate = v_.speed_

        coordinate = 0
        if cla == 'one':
            coordinate = 0
        if cla == 'two':
            coordinate = 960
        if cla == 'three':
            coordinate = 960 * 2
        if cla == 'four':
            coordinate = 960 * 3
        if cla == 'five':
            coordinate = 960 * 4
        if cla == 'six':
            coordinate = 960 * 5

        # if v_.now_arduino == "on":
        #
        #     ser = serial.Serial(arduino_port, baudrate)
        #
        #     moveZ = 1
        #     k_reg = v_.mouse_speed
        #     c_reg = v_.mouse_pm
        #
        #     move_ = False
        #     move_count = 0
        #     while move_ is False:
        #         move_count += 1
        #         if move_count > v_.mouse_move_count:
        #             move_ = True
        #
        #
        #
        #         # 이동 시킬 포인트 계산
        #         x_reg = pos_1 + coordinate - pyautogui.position()[0]
        #         y_reg = pos_2 - pyautogui.position()[1]
        #
        #         if -c_reg < x_reg < c_reg:
        #             moveX = x_reg
        #         elif x_reg > 0:
        #             if x_reg == k_reg:
        #                 moveX = x_reg
        #             else:
        #                 moveX = min(k_reg, x_reg)
        #         else:
        #             if x_reg == -k_reg:
        #                 moveX = x_reg
        #             else:
        #                 moveX = max(-k_reg, x_reg)
        #
        #         if -c_reg < y_reg < c_reg:
        #             moveY = y_reg
        #         elif y_reg > 0:
        #             if y_reg == k_reg:
        #                 moveY = y_reg
        #             else:
        #                 moveY = min(k_reg, y_reg)
        #         else:
        #             if y_reg == -k_reg:
        #                 moveY = y_reg
        #             else:
        #                 moveY = max(-k_reg, y_reg)
        #
        #         data = f'x = {moveX}, y = {moveY}, z = {moveZ}\n'
        #         ser.write(data.encode())
        #         received_data = ser.readline().decode().strip()
        #
        #         if -c_reg < moveX < c_reg and -c_reg < moveY < c_reg:
        #             x_reg = pos_1 + coordinate - pyautogui.position()[0]
        #             y_reg = pos_2 - pyautogui.position()[1]
        #             if -c_reg < x_reg < c_reg and -c_reg < y_reg < c_reg and pyautogui.position()[1] >= 31:
        #                 move_ = True
        #                 data = f'x = {moveX}, y = {moveY}, z = {moveZ}\n'
        #                 ser.write(data.encode())
        #
        #
        #     ser.close()
        #     QTest.qWait(10)
        # else:
        pyautogui.moveTo(pos_1 + random_int() + coordinate, pos_2 + random_int(), 0.1)

    except Exception as e:
        print("error:", e)


def drag_pos_Press():
    try:
        import serial
        import pyautogui

        arduino_port = v_.COM_
        baudrate = v_.speed_

        ser = serial.Serial(arduino_port, baudrate)

        # 마우스 누르기
        moveX = 0
        moveY = 0
        moveZ = 3
        data = f'x = {moveX}, y = {moveY}, z = {moveZ}\n'
        ser.write(data.encode())

        ser.close()
        QTest.qWait(10)

    except Exception as e:
        print("error:", e)


def drag_pos_Release():
    try:
        import serial
        import pyautogui

        arduino_port = v_.COM_
        baudrate = v_.speed_

        ser = serial.Serial(arduino_port, baudrate)
        # 마우스 떼기
        moveX = 0
        moveY = 0
        moveZ = 4
        data = f'x = {moveX}, y = {moveY}, z = {moveZ}\n'
        ser.write(data.encode())

        ser.close()
        QTest.qWait(10)

    except Exception as e:
        print("error:", e)


def drag_pos(pos_1, pos_2, pos_3, pos_4, cla):
    try:
        import pyautogui

        if cla == 'one':
            coordinate = 0
        if cla == 'two':
            coordinate = 960
        if cla == 'three':
            coordinate = 960 * 2
        if cla == 'four':
            coordinate = 960 * 3
        if cla == 'five':
            coordinate = 960 * 4
        if cla == 'six':
            coordinate = 960 * 5

        pyautogui.moveTo(pos_1 + coordinate, pos_2)

        if v_.now_arduino == "on":

            # 마우스 이동
            mouse_move_drag(pos_1, pos_2, cla, 20)

            # 0.1초
            time.sleep(0.1)
            # 마우스 누르기
            drag_pos_Press()
            # # 0.2초
            time.sleep(0.3)
            # 마우스 이동
            mouse_move_drag(pos_3, pos_4, cla, 3)
            # # 0.2초
            time.sleep(0.2)
            # 마우스 떼기
            drag_pos_Release()
            # 0.2초
            time.sleep(0.5)

        else:
            mouse_move_cpp(pos_1, pos_2, cla)
            pyautogui.dragTo(pos_3 + random_int() + coordinate, pos_4 + random_int(), 0.5, button='left')
            time.sleep(0.3)


    except Exception as e:
        print("error:", e)


def drag_pos_py(pos_1, pos_2, pos_3, pos_4, cla):
    try:
        import pyautogui

        if cla == 'one':
            coordinate = 0
        if cla == 'two':
            coordinate = 960
        if cla == 'three':
            coordinate = 960 * 2
        if cla == 'four':
            coordinate = 960 * 3
        if cla == 'five':
            coordinate = 960 * 4
        if cla == 'six':
            coordinate = 960 * 5

        mouse_move_cpp(pos_1, pos_2, cla)
        pyautogui.dragTo(pos_3 + random_int() + coordinate, pos_4 + random_int(), 0.5, button='left')
        time.sleep(0.3)


    except Exception as e:
        print("error:", e)


def drag_pos_click(pos_1, pos_2, pos_3, pos_4, cla):
    try:
        import pyautogui

        if cla == 'one':
            coordinate = 0
        if cla == 'two':
            coordinate = 960
        if cla == 'three':
            coordinate = 960 * 2
        if cla == 'four':
            coordinate = 960 * 3
        if cla == 'five':
            coordinate = 960 * 4
        if cla == 'six':
            coordinate = 960 * 5

        click_pos_2(pos_1, pos_2, cla)

        if v_.now_arduino == "on":

            # 마우스 이동
            mouse_move_drag(pos_1, pos_2, cla, 20)

            # 0.1초
            time.sleep(0.1)
            # 마우스 누르기
            drag_pos_Press()
            # # 0.2초
            time.sleep(0.2)
            # 마우스 이동
            mouse_move_drag(pos_3, pos_4, cla, 5)
            # # 0.2초
            time.sleep(0.2)
            # 마우스 떼기
            drag_pos_Release()
            # 0.2초
            time.sleep(0.5)

        else:
            mouse_move_cpp(pos_1, pos_2, cla)
            pyautogui.dragTo(pos_3 + random_int() + coordinate, pos_4 + random_int(), 0.5, button='left')
            time.sleep(0.3)


    except Exception as e:
        print("error:", e)


def drag_pos_reg(pos_1, pos_2, pos_3, pos_4, cla):
    try:
        import pyautogui

        coordinate = 0
        if cla == 'one':
            coordinate = 0
        if cla == 'two':
            coordinate = 0
        if cla == 'three':
            coordinate = 0
        if cla == 'four':
            coordinate = 0
        if cla == 'five':
            coordinate = 0
        if cla == 'six':
            coordinate = 0

        pyautogui.moveTo(pos_1 + coordinate, pos_2)

        if v_.now_arduino == "on":
            cla = "one"
            # 마우스 이동
            mouse_move_drag_reg(pos_1, pos_2, cla, 20)

            # 0.1초
            time.sleep(0.1)
            # 마우스 누르기
            drag_pos_Press()
            # 0.2초
            time.sleep(0.2)
            # 마우스 이동
            mouse_move_drag_reg(pos_3, pos_4, cla, 5)
            # 0.2초
            time.sleep(0.2)
            # 마우스 떼기
            drag_pos_Release()
            # 0.5초
            time.sleep(0.5)
        else:
            pyautogui.moveTo(pos_1 + random_int() + coordinate, pos_2 + random_int(), 0.5)
            pyautogui.dragTo(pos_3 + random_int() + coordinate, pos_4 + random_int(), 0.5)
            time.sleep(0.3)

    except Exception as e:
        print("error:", e)


def drag_pos_reg_py(pos_1, pos_2, pos_3, pos_4, cla):
    try:
        import pyautogui

        coordinate = 0
        if cla == 'one':
            coordinate = 0
        if cla == 'two':
            coordinate = 0
        if cla == 'three':
            coordinate = 0
        if cla == 'four':
            coordinate = 0
        if cla == 'five':
            coordinate = 0
        if cla == 'six':
            coordinate = 0

        pyautogui.moveTo(pos_1 + random_int() + coordinate, pos_2 + random_int(), 0.5)
        pyautogui.dragTo(pos_3 + random_int() + coordinate, pos_4 + random_int(), 0.5)
        time.sleep(0.3)

    except Exception as e:
        print("error:", e)


def drag_pos_reg_click(pos_1, pos_2, pos_3, pos_4, cla):
    try:
        import pyautogui

        coordinate = 0
        if cla == 'one':
            coordinate = 0
        if cla == 'two':
            coordinate = 0
        if cla == 'three':
            coordinate = 0
        if cla == 'four':
            coordinate = 0
        if cla == 'five':
            coordinate = 0
        if cla == 'six':
            coordinate = 0

        click_pos_reg(pos_1, pos_2, cla)

        if v_.now_arduino == "on":
            cla = "one"
            # 마우스 이동
            mouse_move_drag_reg(pos_1, pos_2, cla, 20)

            # 0.1초
            time.sleep(0.1)
            # 마우스 누르기
            drag_pos_Press()
            # 0.2초
            time.sleep(0.2)
            # 마우스 이동
            mouse_move_drag_reg(pos_3, pos_4, cla, 5)
            # 0.2초
            time.sleep(0.2)
            # 마우스 떼기
            drag_pos_Release()
            # 0.5초
            time.sleep(0.5)
        else:
            pyautogui.moveTo(pos_1 + random_int() + coordinate, pos_2 + random_int(), 0.5)
            pyautogui.dragTo(pos_3 + random_int() + coordinate, pos_4 + random_int(), 0.5)
            time.sleep(0.3)

    except Exception as e:
        print("error:", e)


# def text_check(posX1, posY1, posX2, posY2, text, method, method_pos):
#     try:
#         isClick = False
#         pos = (posX1, posY1, posX2 - posX1, posY2 - posY1)
#         while isClick is False:
#             pic = pyautogui.screenshot("asd.png", region=pos)
#             pic_ = numpy.array(pic)
#             # result = reader.readtext(pic_)
#             for txt in result:
#                 if txt is not None:
#                     print(txt[1])
#                     for text_ in text:
#                         if txt[1] == text_:
#                             print("aaa!!")
#                             method(method_pos)
#                             isClick = True
#     except Exception as e:
#         print(e)

def text_check_potion(posX1, posY1, posX2, posY2, cla):
    try:
        from PIL import ImageGrab
        from functools import partial
        import pyautogui
        import pytesseract

        ImageGrab.grab = partial(ImageGrab.grab, all_screens=True)

        potion = 0

        # result = pyautogui.locateCenterOnScreen(img, region=(a + plus, b, c - a + 10, d - b + 10),
        #                                         confidence=0.7)

        img = pyautogui.screenshot('asd.png', region=(get_region(posX1, posY1, posX2, posY2, cla)))
        white_img = image_processing(img, (148, 148, 148), (255, 255, 255))
        potion_count_ = pytesseract.image_to_string(white_img, lang=None)
        # print("text_check_potion", potion_count_)

        result_num_in = in_number_check(potion_count_)
        if result_num_in == True:
            potion = change_number(potion_count_)
            potion_bloon = potion.isdigit()
            if potion_bloon == True:
                potion = int(potion)
            else:
                print("potion => 숫자 아님")

        return potion
    except Exception as e:
        print(e)
        return 0



def text_check_get_black_white(posX1, posY1, posX2, posY2, cla):
    try:
        from PIL import ImageGrab
        from functools import partial
        import cv2
        import pytesseract
        import numpy
        import pyautogui

        ImageGrab.grab = partial(ImageGrab.grab, all_screens=True)

        coordinate = 0
        if cla == 'one':
            coordinate = 0
        if cla == 'two':
            coordinate = 960
        if cla == 'three':
            coordinate = 960 * 2
        if cla == 'four':
            coordinate = 960 * 3
        if cla == 'five':
            coordinate = 960 * 4
        if cla == 'six':
            coordinate = 960 * 5

        # 화면의 지정된 부분 캡처
        screenshot = pyautogui.screenshot(region=(posX1 + coordinate, posY1, posX2 - posX1, posY2 - posY1))

        # 이미지를 흑백으로 변환
        screenshot = screenshot.convert('L')

        # 이미지에서 텍스트 추출
        current_text = pytesseract.image_to_string(screenshot, config='--psm 6').strip()

        this_text = current_text

        print("this_text", this_text)

        ##
        return this_text
    except Exception as e:
        print(e)
        return 0

def text_check_get_black_white(posX1, posY1, posX2, posY2, cla):
    try:
        from PIL import ImageGrab
        from functools import partial
        import cv2
        import pytesseract
        import numpy
        import pyautogui

        ImageGrab.grab = partial(ImageGrab.grab, all_screens=True)

        coordinate = 0
        if cla == 'one':
            coordinate = 0
        if cla == 'two':
            coordinate = 960
        if cla == 'three':
            coordinate = 960 * 2
        if cla == 'four':
            coordinate = 960 * 3
        if cla == 'five':
            coordinate = 960 * 4
        if cla == 'six':
            coordinate = 960 * 5

        # 화면의 지정된 부분 캡처
        screenshot = pyautogui.screenshot(region=(posX1, posY1, posX2 - posX1, posY2 - posY1))

        # 이미지를 흑백으로 변환
        screenshot = screenshot.convert('L')

        # 이미지에서 텍스트 추출
        current_text = pytesseract.image_to_string(screenshot, config='--psm 6').strip()

        this_text = current_text

        print("this_text", this_text)

        ##
        return this_text
    except Exception as e:
        print(e)
        return 0

def text_check_get(posX1, posY1, posX2, posY2, cla):
    try:
        from PIL import ImageGrab
        from functools import partial
        import cv2
        import pytesseract
        import numpy
        import pyautogui

        ImageGrab.grab = partial(ImageGrab.grab, all_screens=True)

        coordinate = 0
        if cla == 'one':
            coordinate = 0
        if cla == 'two':
            coordinate = 960
        if cla == 'three':
            coordinate = 960 * 2
        if cla == 'four':
            coordinate = 960 * 3
        if cla == 'five':
            coordinate = 960 * 4
        if cla == 'six':
            coordinate = 960 * 5
        pos = (posX1 + coordinate, posY1, posX2 - posX1, posY2 - posY1)
        pyautogui.screenshot("asd.png", region=pos)
        pic = cv2.imread("asd.png", cv2.IMREAD_COLOR)  # 사진을 컬러로 읽어오기
        cv2.imwrite("asd.png", pic)
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
        pic_ = numpy.array(pic)
        result = pytesseract.image_to_string(pic_, lang='kor+eng')

        ##
        return result
    except Exception as e:
        print(e)
        return 0


def text_check_get_reg(posX1, posY1, posX2, posY2):
    try:
        from PIL import ImageGrab
        from functools import partial
        import cv2
        import pytesseract
        import numpy
        import pyautogui

        ImageGrab.grab = partial(ImageGrab.grab, all_screens=True)

        coordinate = 0
        pos = (posX1 + coordinate, posY1, posX2 - posX1, posY2 - posY1)
        pyautogui.screenshot("asd.png", region=pos)
        pic = cv2.imread("asd.png", cv2.IMREAD_COLOR)  # 사진을 컬러로 읽어오기
        cv2.imwrite("asd.png", pic)
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
        pic_ = numpy.array(pic)
        result = pytesseract.image_to_string(pic_, lang='kor+eng')

        ##
        return result
    except Exception as e:
        print(e)
        return 0


def text_check_get_num(posX1, posY1, posX2, posY2, cla):
    try:
        from PIL import ImageGrab
        from functools import partial
        import cv2
        import pytesseract
        import numpy
        from PIL import Image
        import pyautogui
        # color change
        coordinate = 0
        if cla == 'one':
            coordinate = 0
        if cla == 'two':
            coordinate = 960
        if cla == 'three':
            coordinate = 960 * 2
        if cla == 'four':
            coordinate = 960 * 3
        if cla == 'five':
            coordinate = 960 * 4
        if cla == 'six':
            coordinate = 960 * 5
        pos = (posX1 + coordinate, posY1, posX2 - posX1, posY2 - posY1)
        pyautogui.screenshot("asd.png", region=pos)
        pic = cv2.imread("asd.png", cv2.IMREAD_COLOR)  # 사진을 컬러로 읽어오기
        cv2.imwrite("asd.png", pic)
        ##
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
        # path = Image.open(r'asd.png')
        pic_ = numpy.array(pic)
        rgb_image = cv2.cvtColor(pic_, cv2.COLOR_BGR2RGB)
        result = pytesseract.image_to_string(rgb_image, config='--psm 6')

        ##
        return result
    except Exception as e:
        print(e)
        return 0


def text_check_get_reg_num(posX1, posY1, posX2, posY2):
    try:
        from PIL import Image
        from PIL import ImageGrab
        from functools import partial
        import cv2
        import pytesseract
        import numpy
        import pyautogui

        ImageGrab.grab = partial(ImageGrab.grab, all_screens=True)

        coordinate = 0
        pos = (posX1 + coordinate, posY1, posX2 - posX1, posY2 - posY1)
        pyautogui.screenshot("asd.png", region=pos)
        pic = cv2.imread("asd.png", cv2.IMREAD_COLOR)  # 사진을 컬러로 읽어오기
        cv2.imwrite("asd.png", pic)
        ##
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
        # path = Image.open(r'asd.png')
        pic_ = numpy.array(pic)
        rgb_image = cv2.cvtColor(pic_, cv2.COLOR_BGR2RGB)
        result = pytesseract.image_to_string(rgb_image, config='--psm 6')

        ##
        return result
    except Exception as e:
        print(e)
        return 0
    except Exception as e:
        print(e)
        return 0


def text_check_get_2(posX1, posY1, posX2, posY2, cla):
    try:
        from PIL import ImageGrab
        from functools import partial
        import cv2
        import pytesseract
        import numpy
        import pyautogui
        coordinate = 0
        if cla == 'one':
            coordinate = 0
        if cla == 'two':
            coordinate = 960
        if cla == 'three':
            coordinate = 960 * 2
        if cla == 'four':
            coordinate = 960 * 3
        if cla == 'five':
            coordinate = 960 * 4
        if cla == 'six':
            coordinate = 960 * 5
        isClick = False
        pos = (posX1 + coordinate, posY1, posX2 - posX1, posY2 - posY1)
        pyautogui.screenshot("asd.png", region=pos)
        pic = cv2.imread("asd.png", cv2.IMREAD_COLOR)  # 사진을 컬러로 읽어오기
        cv2.imwrite("asd.png", pic)
        ##
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
        # path = Image.open(r'asd.png')
        pic_ = numpy.array(pic)
        rgb_image = cv2.cvtColor(pic_, cv2.COLOR_BGR2RGB)
        result = pytesseract.image_to_string(rgb_image, lang='kor+eng')

        ##
        return result
    except Exception as e:
        print(e)
        return 0


def text_check_get_3(posX1, posY1, posX2, posY2, color, cla):
    try:
        from PIL import ImageGrab
        from functools import partial
        import cv2
        import pytesseract
        import numpy
        from PIL import Image
        import pyautogui
        # color change
        coordinate = 0
        if cla == 'one':
            coordinate = 0
        if cla == 'two':
            coordinate = 960
        if cla == 'three':
            coordinate = 960 * 2
        if cla == 'four':
            coordinate = 960 * 3
        if cla == 'five':
            coordinate = 960 * 4
        if cla == 'six':
            coordinate = 960 * 5
        pos = (posX1 + coordinate, posY1, posX2 - posX1, posY2 - posY1)
        pyautogui.screenshot("asd.png", region=pos)
        pic = cv2.imread("asd.png", cv2.IMREAD_COLOR)  # 사진을 컬러로 읽어오기
        cv2.imwrite("asd.png", pic)
        ##
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
        path = Image.open(r'asd.png')
        pic_ = numpy.array(pic)
        if color == 0:
            rgb_image = cv2.cvtColor(pic_, cv2.COLOR_BGR2RGB)
        if color == 1:
            rgb_image = cv2.cvtColor(pic_, cv2.COLOR_BGR2GRAY)
        if color == 2:
            rgb_image = cv2.cvtColor(pic_, cv2.COLOR_BGR2HSV)
        if color == 3:
            rgb_image = cv2.cvtColor(pic_, cv2.COLOR_BGR2YUV)
        if color == 4:
            rgb_image = cv2.cvtColor(pic_, cv2.COLOR_BGR2RGB)
        if color == 5:
            rgb_image = cv2.cvtColor(pic_, cv2.COLOR_BGR2RGB)
        if color == 6:
            rgb_image = cv2.cvtColor(pic_, cv2.COLOR_BGR2RGB)
        result = pytesseract.image_to_string(rgb_image, lang='kor+eng')

        ##
        return result
    except Exception as e:
        print(e)
        return 0


def text_check_get_4(posX1, posY1, posX2, posY2, color, cla):
    try:
        from PIL import ImageGrab
        from functools import partial
        import numpy as np
        import cv2
        import pytesseract
        import numpy
        import pyautogui
        # color change
        coordinate = 0
        if cla == 'one':
            coordinate = 0
        if cla == 'two':
            coordinate = 960
        if cla == 'three':
            coordinate = 960 * 2
        if cla == 'four':
            coordinate = 960 * 3
        if cla == 'five':
            coordinate = 960 * 4
        if cla == 'six':
            coordinate = 960 * 5
        pos = (posX1 + coordinate, posY1, posX2 - posX1, posY2 - posY1)
        pyautogui.screenshot("asd.png", region=pos)
        pic = cv2.imread("asd.png")
        cv2.imwrite("asd.png", pic)
        ##
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
        # path = Image.open(r'asd.png')
        pic_ = numpy.array(pic)

        rgb_image_ = cv2.cvtColor(pic_, cv2.COLOR_BGR2HSV)

        lower_yellow = np.array([60, 100, 100])
        upper_yellow = np.array([90, 255, 255])

        lower_green = np.array([50, 100, 100])
        upper_green = np.array([70, 255, 255])

        lower_red = np.array([-10, 100, 100])
        upper_red = np.array([10, 255, 255])

        if color == 0:
            rgb_image_ready = cv2.inRange(rgb_image_, lower_yellow, upper_yellow)
            rgb_image = cv2.bitwise_and(pic, pic, mask=rgb_image_ready)
        if color == 1:
            rgb_image_ready = cv2.inRange(rgb_image_, lower_green, upper_green)
            rgb_image = cv2.bitwise_and(pic, pic, mask=rgb_image_ready)
        if color == 2:
            rgb_image_ready = cv2.inRange(rgb_image_, lower_red, upper_red)
            rgb_image = cv2.bitwise_and(pic, pic, mask=rgb_image_ready)
        result = pytesseract.image_to_string(rgb_image, lang='kor+eng')

        cv2.imshow('img_color', pic)

        ##
        return result
    except Exception as e:
        print(e)
        return 0


def how_many_pic(posX1, posY1, posX2, posY2, address, cla):
    try:
        from PIL import ImageGrab
        from functools import partial
        import cv2
        import pytesseract
        import numpy as np
        from PIL import Image
        import pyautogui

        ImageGrab.grab = partial(ImageGrab.grab, all_screens=True)

        coordinate = 0
        if cla == 'one':
            coordinate = 0
        if cla == 'two':
            coordinate = 960
        if cla == 'three':
            coordinate = 960 * 2
        if cla == 'four':
            coordinate = 960 * 3
        if cla == 'five':
            coordinate = 960 * 4
        if cla == 'six':
            coordinate = 960 * 5

        full_path = address  # '완료' 그림 갯수 파악
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        many = 0
        before = 0
        after = 0
        print("hihihihihi", coordinate)
        for list in pyautogui.locateAllOnScreen(img, region=(posX1 + coordinate, posY1, posX2 - posX1, posY2 - posY1),
                                                confidence=0.75):
            # print("list", list)
            after = list.top
            if before != after:
                before = after
                many += 1

        ##
        return many
    except Exception as e:
        print(e)
        return 0

################### 아두이노 키보드 #####################







# ============================================================
# Arduino Leonardo HID - 확장 키보드/마우스 프로토콜 래퍼
#   - Firmware 프로토콜:
#       KEY <combo>        (예: KEY CTRL+C, KEY ALT+1, KEY TAB)
#       TEXT <text>        (그대로 타이핑)
#       KD <key> / KU <key>  (키다운/키업: 홀드 지원)
#       MC L/R             (마우스 클릭)
#       MD L/R / MU L/R     (마우스 다운/업)
#   - 중요:
#       click_pos_2()는 내부에서 serial을 오래 잡을 수 있음.
#       아래 함수들은 "open/write/close per call"로 COM 충돌을 줄임.
# ============================================================

_ARDUINO_SER = None  # (호환용) 더 이상 캐시로 쓰지 않음


def _arduino_open_serial():
    """포트를 새로 열지 않고, 기존에 열린 포트가 있다면 재사용함"""
    global _SHARED_SER
    import serial
    import time
    import variable as v_

    # 이미 포트가 열려 있고 정상이라면 그대로 반환
    if _SHARED_SER is not None and _SHARED_SER.is_open:
        return _SHARED_SER

    # 포트가 없거나 닫힌 경우에만 새로 연결 시도
    try:
        # v_.COM_과 v_.speed_ 값을 사용
        _SHARED_SER = serial.Serial(v_.COM_, v_.speed_, timeout=0.01)
        time.sleep(1.0) # 아두이노 부팅 대기
        print(f"시스템: 아두이노 {v_.COM_} 연결 성공")
        return _SHARED_SER
    except Exception as e:
        print(f"시리얼 오픈 에러: {e}")
        return None


def _arduino_close_serial(ser=None):
    """Close a serial connection."""
    try:
        if ser is not None:
            ser.close()
    except Exception:
        pass


def _arduino_write_line(line):
    """모든 아두이노 명령 전송의 단일 통로"""
    try:
        ser = _arduino_open_serial()
        if ser:
            if not line.endswith('\n'):
                line += '\n'
            ser.write(line.encode())
    except Exception as e:
        print(f"명령 전송 중 오류: {e}")
        global _SHARED_SER
        _SHARED_SER = None # 에러 발생 시 초기화하여 다음 호출 때 재연결 유도


def _arduino_try_readline(max_wait_sec: float = 0.8) -> str:
    """Try to read a line from Arduino (open/read/close). Returns '' if nothing."""
    import time

    ser = None
    try:
        ser = _arduino_open_serial()
        deadline = time.time() + float(max_wait_sec)
        while time.time() < deadline:
            try:
                if ser.in_waiting:
                    return ser.readline().decode("utf-8", errors="ignore").strip()
            except Exception:
                return ""
            time.sleep(0.02)
        return ""
    finally:
        _arduino_close_serial(ser)


def wait_ms(ms: int):
    """Qt 환경이면 QTest.qWait, 아니면 time.sleep."""
    try:
        QTest.qWait(int(ms))
    except Exception:
        import time
        time.sleep(max(0.0, float(ms) / 1000.0))


def arduino_key(combo: str, wait_ack: bool = False) -> bool:
    """Send KEY command.

    combo examples:
      - 'a' .. 'z'
      - 'ALT+1'
      - 'CTRL+C'
      - 'CTRL+SHIFT+ESC'
      - 'ENTER', 'TAB', 'ESC', 'LEFT', 'RIGHT', 'F1'..'F12'
    """
    # Arduino off면 OS 키입력으로 fallback
    if getattr(v_, "now_arduino", "off") != "on":
        try:
            import pyautogui
            if "+" in combo:
                pyautogui.hotkey(*[t.strip().lower() for t in combo.split("+") if t.strip()])
            else:
                pyautogui.press(combo.strip().lower())
            return True
        except Exception:
            return False

    combo = (combo or "").strip()
    if not combo:
        return False

    _arduino_write_line(f"KEY {combo}")

    if not wait_ack:
        return True

    # Firmware prints KEY_ERR only on failure; no positive ACK.
    resp = _arduino_try_readline(max_wait_sec=0.8)
    return resp != "KEY_ERR"


def arduino_text(text: str, wait_ok: bool = True) -> bool:
    """Send TEXT command (types the payload as-is)."""
    if getattr(v_, "now_arduino", "off") != "on":
        try:
            import pyautogui
            pyautogui.write(text)
            return True
        except Exception:
            return False

    text = (text or "")
    if text.strip() == "":
        return False

    _arduino_write_line(f"TEXT {text}")

    if not wait_ok:
        return True

    # Firmware prints TEXT_OK after printing
    resp = _arduino_try_readline(max_wait_sec=1.2)
    return (resp == "TEXT_OK") or (resp == "")


def arduino_press(key: str) -> bool:
    """Tap a key (press+release).  예: arduino_press('a'), arduino_press('TAB'), arduino_press('r')"""
    return arduino_key(key, wait_ack=False)


def arduino_hotkey(*keys: str) -> bool:
    """Convenience: arduino_hotkey('ctrl','c') => KEY CTRL+C"""
    combo = "+".join([str(k).strip().upper() for k in keys if str(k).strip()])
    return arduino_key(combo, wait_ack=False)


def arduino_typing(s: str) -> bool:
    """Typing helper: uses TEXT for longer strings; KEY for single printable character."""
    s = "" if s is None else str(s)
    if len(s) == 1:
        return arduino_key(s, wait_ack=False)
    return arduino_text(s, wait_ok=True)


def arduino_keydown(key: str) -> bool:
    """Hold key down. 예: arduino_keydown('W')"""
    key = (key or "").strip()
    if not key:
        return False
    try:
        _arduino_write_line(f"KD {key}")
        return True
    except Exception as e:
        print(e)
        return False


def arduino_keyup(key: str) -> bool:
    """Release key. 예: arduino_keyup('W')"""
    key = (key or "").strip()
    if not key:
        return False
    try:
        _arduino_write_line(f"KU {key}")
        return True
    except Exception as e:
        print(e)
        return False


def hold_key_ms(key: str, ms: int):
    """key를 ms 동안 홀드."""
    arduino_keydown(key)
    try:
        wait_ms(int(ms))
    finally:
        # keyup은 실패 시 한 번 더 시도 (게임/USB 상황에 따라 드물게 누락 방지)
        try:
            arduino_keyup(key)
        except Exception:
            pass
        wait_ms(20)
        try:
            arduino_keyup(key)
        except Exception:
            pass


def arduino_mouseclick_left() -> bool:
    """통합된 시리얼 통로를 사용하여 이동 없이 좌클릭 실행"""
    try:
        # _arduino_write_line 대신 통합 전송 함수 사용
        send_arduino_cmd("MC L")
        return True
    except Exception as e:
        print(f"좌클릭 에러: {e}")
        return False


def arduino_mousedown_left():
    """마우스 왼쪽 버튼 누르기 (홀딩 시작)"""
    send_arduino_cmd("x = 0, y = 0, z = 3")

def arduino_mouseup_left():
    """마우스 왼쪽 버튼 떼기 (홀딩 해제)"""
    send_arduino_cmd("x = 0, y = 0, z = 4")

def arduino_right_click():
    """아두이노를 이용한 마우스 오른쪽 클릭 실행 (단일 명령 통합)"""
    try:
        # z=5, z=6을 나누어 보내는 대신 MC R 명령 한 번으로 처리
        send_arduino_cmd("MC R")
        print("Arduino: 마우스 오른쪽 클릭 실행 (MC R)")
    except Exception as e:
        print(f"arduino_right_click Error: {e}")

def arduino_right_down():
    """오른쪽 버튼 누르기"""
    send_arduino_cmd("x = 0, y = 0, z = 5")

def arduino_right_up():
    """오른쪽 버튼 떼기"""
    send_arduino_cmd("x = 0, y = 0, z = 6")

def arduino_click():
    """(호환) 이동 없이 좌클릭 1회."""
    return arduino_mouseclick_left()



def sync_arduino_command(command):
    """동기화 전용: 포트를 열어두고 명령만 전송"""
    global _SYNC_SER
    import serial
    try:
        if _SYNC_SER is None or not _SYNC_SER.is_open:
            _SYNC_SER = serial.Serial(v_.COM_, v_.speed_, timeout=0.05)

        _SYNC_SER.write(f"{command}\n".encode())
    except Exception as e:
        print(f"Sync Serial Error: {e}")
        if _SYNC_SER:
            _SYNC_SER.close()
            _SYNC_SER = None


def get_sync_ser():
    """동기화 전용: 포트를 한 번만 열어서 계속 사용"""
    global _SYNC_SER
    import serial
    if _SYNC_SER is None or not _SYNC_SER.is_open:
        try:
            # 타임아웃을 짧게 주어 반응 속도를 높입니다.
            _SYNC_SER = serial.Serial(v_.COM_, v_.speed_, timeout=0.01)
        except Exception as e:
            print(f"시리얼 포트 오픈 에러: {e}")
            return None
    return _SYNC_SER


# 파일 최상단 전역 변수 영역
_SHARED_SER = None


def get_arduino_ser():
    """모든 기능이 공유하는 단일 시리얼 객체 반환 (싱글톤 패턴)"""
    global _SHARED_SER
    import serial
    import variable as v_
    import time

    # 포트가 없거나 닫혀있을 때만 새로 생성
    if _SHARED_SER is None or not _SHARED_SER.is_open:
        try:
            # 9600보다 빠른 115200 권장 (아두이노 소스도 수정 필요)
            _SHARED_SER = serial.Serial(v_.COM_, v_.speed_, timeout=0.01)
            time.sleep(1.0)  # 아두이노 리셋 대기 시간 필수
            print(f"시스템: 아두이노 연결 성공 ({v_.COM_})")
        except Exception as e:
            print(f"시리얼 연결 실패: {e}")
            return None
    return _SHARED_SER


def send_arduino_cmd(cmd):
    """모든 아두이노 명령(마우스/키보드)을 이 함수로 통합 전송"""
    ser = get_arduino_ser()
    if ser:
        try:
            # 명령어 끝에 개행문자(\n)가 있어야 아두이노가 인식함
            ser.write(f"{cmd}\n".encode())
        except Exception as e:
            print(f"명령 전송 실패: {e}")
            global _SHARED_SER
            _SHARED_SER = None  # 에러 발생 시 초기화하여 다음 호출 때 재연결 유도

def arduino_key_down(key):
    send_arduino_cmd(f"KD {key.upper()}")

def arduino_key_up(key):
    send_arduino_cmd(f"KU {key.upper()}")

def arduino_panic():
    """모든 키/마우스 입력 강제 해제 (더 강력한 버전)"""
    # 1. 자주 사용하는 키들을 명시적으로 해제 명령 전송
    target_keys = ['w', 'a', 's', 'd', 'f', 'b', 'TAB', 'r', 'q', 'e', 'T', '`', '7', '8']
    for key in target_keys:
        send_arduino_cmd(f"KU {key}")

    # 2. 마우스 버튼 해제 (Z=4: 좌클릭Up, Z=6: 우클릭Up)
    send_arduino_cmd("x = 0, y = 0, z = 4")
    send_arduino_cmd("x = 0, y = 0, z = 6")

    # 3. 마지막으로 아두이노 자체 패닉 명령어 전송
    send_arduino_cmd("PANIC")
    print("시스템: 아두이노 모든 입력 강제 해제 완료")

def click_pos_abs(pos_1, pos_2, click):
    """공유 시리얼을 사용하여 절대 좌표 클릭"""
    import pyautogui
    try:
        pos_1, pos_2 = int(pos_1), int(pos_2)
        if v_.now_arduino == "on":
            # 1. 이동 명령 (Z=1: 이동)
            send_arduino_cmd(f"x = {pos_1 - pyautogui.position()[0]}, y = {pos_2 - pyautogui.position()[1]}, z = 1")
            time.sleep(0.05)
            # 2. 클릭 명령 (Z=3: Down, Z=4: Up)
            if click == "left":
                arduino_mouseclick_left()
            elif click == "right":
                arduino_right_click()
        else:
            pyautogui.click(pos_1, pos_2)
    except Exception as e:
        print(f"click_pos_abs Error: {e}")


# ============================================================
# MicroStepper: "사람처럼 보이게" 짧게 움직이되, 항상 제자리 복귀
#   - 핵심: 전진만 계속 누르면 사냥터 이탈함 -> 반드시 "왕복(pair)"로 움직임.
#   - r(기본공격)가 사거리로 접근해주므로, 스텝은 '아주 가끔'만(쿨다운) 사용.
# ============================================================

class MicroStepper:
    def __init__(
        self,
        max_drift_units: int = 2,
        fwd_ms_range=(90, 140),
        back_ms_range=(90, 140),
        left_ms_range=(80, 130),
        right_ms_range=(80, 130),
        pause_ms_range=(60, 120),
        step_cooldown_ms=(1400, 2600),
        prefer_strafe: float = 0.7,
    ):
        """
        prefer_strafe: 0~1.0 (높을수록 A/D 위주, W/S는 덜 씀)
        """
        import random
        self._rand = random
        self.max_drift_units = int(max_drift_units)
        self.fwd_ms_range = fwd_ms_range
        self.back_ms_range = back_ms_range
        self.left_ms_range = left_ms_range
        self.right_ms_range = right_ms_range
        self.pause_ms_range = pause_ms_range
        self.step_cooldown_ms = step_cooldown_ms
        self.prefer_strafe = float(prefer_strafe)

        self._next_allowed_ts = 0.0
        self._drift_fb = 0  # forward/back drift units ( + forward, - back )
        self._drift_lr = 0  # left/right drift units ( + right, - left )

    def _now(self) -> float:
        import time
        return time.time()

    def _ms_rand(self, r):
        a, b = int(r[0]), int(r[1])
        if a > b:
            a, b = b, a
        return self._rand.randint(a, b)

    def _cooldown_ok(self) -> bool:
        return self._now() >= self._next_allowed_ts

    def _arm_cooldown(self):
        cd = self._ms_rand(self.step_cooldown_ms)
        self._next_allowed_ts = self._now() + (cd / 1000.0)

    def _pause(self):
        wait_ms(self._ms_rand(self.pause_ms_range))

    def _pair_hold(self, key1: str, ms1: int, key2: str, ms2: int):
        """
        key1 홀드 후 key2 홀드(반대 방향) -> 제자리 복귀 목적.
        """
        hold_key_ms(key1, ms1)
        self._pause()
        hold_key_ms(key2, ms2)

    def maybe_step(self, force: bool = False):
        """
        쿨다운이 끝났으면 '짧은 왕복 움직임' 1회를 수행.
        - force=True면 쿨다운 무시.
        """
        if (not force) and (not self._cooldown_ok()):
            return

        # drift가 한쪽으로 누적되면 반대 방향 우선 (안전장치)
        if self._drift_fb >= self.max_drift_units:
            ms = self._ms_rand(self.back_ms_range)
            self._pair_hold("S", ms, "W", ms)
            self._drift_fb -= 1
            self._arm_cooldown()
            return
        if self._drift_fb <= -self.max_drift_units:
            ms = self._ms_rand(self.fwd_ms_range)
            self._pair_hold("W", ms, "S", ms)
            self._drift_fb += 1
            self._arm_cooldown()
            return
        if self._drift_lr >= self.max_drift_units:
            ms = self._ms_rand(self.left_ms_range)
            self._pair_hold("A", ms, "D", ms)
            self._drift_lr -= 1
            self._arm_cooldown()
            return
        if self._drift_lr <= -self.max_drift_units:
            ms = self._ms_rand(self.right_ms_range)
            self._pair_hold("D", ms, "A", ms)
            self._drift_lr += 1
            self._arm_cooldown()
            return

        # 기본: 대부분은 좌우(A/D) 왕복, 가끔만 전후(W/S) 왕복
        use_strafe = (self._rand.random() < self.prefer_strafe)
        if use_strafe:
            ms = self._ms_rand(self.left_ms_range)
            if self._rand.random() < 0.5:
                self._pair_hold("A", ms, "D", ms)
                # net zero지만 drift safety용으로 약간 누적/감쇠 시뮬레이션
                self._drift_lr += 0
            else:
                self._pair_hold("D", ms, "A", ms)
                self._drift_lr += 0
        else:
            ms = self._ms_rand(self.fwd_ms_range)
            if self._rand.random() < 0.5:
                self._pair_hold("W", ms, "S", ms)
                self._drift_fb += 0
            else:
                self._pair_hold("S", ms, "W", ms)
                self._drift_fb += 0

        self._arm_cooldown()

def hold_move_and_attack(move_key: str = "A", hold_ms: int = 140, attack_key: str = "r", attack_count: int = 1):
    """
    '움직임 + 공격'을 한 번에 호출하고 싶을 때 사용.
    - move_key: W/S/A/D
    - hold_ms: 움직임 유지 시간
    - attack_key: 기본공격 키(현재 r)
    """
    hold_key_ms(move_key, int(hold_ms))
    wait_ms(60)
    for _ in range(max(1, int(attack_count))):
        arduino_press(attack_key)
        wait_ms(80)
