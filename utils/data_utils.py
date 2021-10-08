import cv2
import math


def get_mp4_length(file_path):
    cap = cv2.VideoCapture(file_path)
    if cap.isOpened():  # 当成功打开视频时cap.isOpened()返回True,否则返回False
        # get方法参数按顺序对应下表（从0开始编号)
        rate = cap.get(5)  # 帧速率
        frame_number = cap.get(7)  # 视频文件的帧数
        seconds = frame_number / rate
        return seconds
    else:
        print("NOOOOOOOOOOOO!")
        return None


def translate_seconds_to_hms(seconds, str=True):
    h = seconds // 3600
    m = seconds % 3600 // 60
    s = seconds % 60
    if str:
        return '{:.0f}时{:.0f}分{:.2f}秒'.format(h, m, s)
    else:
        return h, m, s


def num2str(self, num):
    return ("{}".format(math.floor(num))).zfill(2)


def num2second(num):
    h = num2str(num / 60 / 60)
    m = num2str(num / 60)
    s = num2str(num % 60)
    return "{}:{}:{}".format(h, m, s)