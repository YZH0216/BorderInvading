import os
import subprocess
import cv2
import math
import shutil
import random
import numpy as np


class FileCheck():

    def get_mp4_length(self, file_path):

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

    def translate_seconds_to_hms(self, seconds, str=True):
        h = seconds // 3600
        m = seconds % 3600 // 60
        s = seconds % 60
        if str:
            return '{:.0f}时{:.0f}分{:.2f}秒'.format(h, m, s)
        else:
            return h, m, s

    def num2str(self, num):
        return ("{}".format(math.floor(num))).zfill(2)

    def num2second(self, num):
        h = self.num2str(num / 60 / 60)
        m = self.num2str(num / 60)
        s = self.num2str(num % 60)
        return "{}:{}:{}".format(h, m, s)

    def cut(self, begin, duration):
        # path下有很多文件夹，获取这些文件夹下（不穿透）的视频长度总和

        root = os.getcwd()
        nParent = os.path.sep.join((root, "cutted"))

        if os.path.exists(nParent):
            shutil.rmtree(nParent)

        os.makedirs(nParent)
        root = os.path.join(root, 'video_datasets/listed_converted')
        for parent, dirs, fs in os.walk(root):
            for f in fs:
                if f.endswith(".mp4"):
                    length = self.get_mp4_length(os.path.join(root, f))
                    print("f {}, len = {}".format(f, length))
                    nLen = begin + duration
                    oldPath = os.path.sep.join((root, f))
                    newPath = os.path.sep.join((nParent, f))

                    start = self.num2second(begin)
                    last = self.num2second(nLen)

                    # cmd = "ffmpeg  -y -ss " + start + "  -to " + \
                    #       last + " -i " + oldPath + " -c copy " + newPath
                    cmd = "ffmpeg  -ss " + start + " -i " + oldPath + " -t " + last + " " + newPath
                    print(cmd)
                    subprocess.call(cmd, shell=True)
                    #print("cmd {}".format(cmd))
                    pass
            break
    def random_cut(self, times, duration):
        len_of_videos = []
        root = os.getcwd()
        nParent = os.path.sep.join((root, "cutted"))

        if os.path.exists(nParent):
            shutil.rmtree(nParent)

        os.makedirs(nParent)
        root = os.path.join(root, 'video_datasets/listed_converted')
        for time in range(times):
            random_file = random.sample(os.listdir(root), 1)[0]
            random_file_path = os.path.join(root, random_file)
            length = self.get_mp4_length(os.path.join(root, random_file))
            if(length > duration + 2):
                print(random_file)
                random_start = random.randint(0, int(length - duration - 2))
            else:
                continue
            oldPath = os.path.sep.join((root, random_file))
            newPath = os.path.sep.join((nParent, str(time + 1) + ".mp4"))

            start = self.num2second(random_start)
            last = self.num2second(random_start + duration + 0)
            # cmd = "ffmpeg  -y -ss " + start + "  -to " + \
            #       last + " -i " + oldPath + " -c copy " + newPath
            cmd = "ffmpeg  -i " + oldPath + " -ss " + start + " -to " + last + " " + newPath + " -y"
            subprocess.call(cmd, shell=True)
            length2 = self.get_mp4_length(os.path.join(nParent, str(time + 1) + ".mp4"))
            len_of_videos.append(length2)
        #     print("=================")
        #     print(cmd)
        #
        #     print(random_file)
        #     print(start, last)
        #     print(length2)
        #     print("=================")
        print("Cut Finished!!!!!!")
        # print(np.mean(len_of_videos))
        # print(len_of_videos)
        #     # print("cmd {}".format(cmd))

if __name__ == "__main__":
    entity = FileCheck()
    entity.random_cut(100, 10)