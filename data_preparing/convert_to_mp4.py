import os
import tqdm
import subprocess
project_dir = '/home/zhenhao/Documents/Projects/BorderInvading/'
dataset_dir = 'video_datasets/to_be_converted'
save_dir = 'video_datasets/converted'
final_dir = 'video_datasets/listed_converted'

to_be_converted = os.path.join(project_dir, dataset_dir)
converted = os.path.join(project_dir, save_dir)
listed_converted = os.path.join(project_dir, final_dir)

if(os.path.exists(converted)):
    os.system("rm -rf " + converted)
    os.system("mkdir -p " + converted)
else:
    os.system("mkdir -p " + converted)

if(os.path.exists(listed_converted)):
    os.system("rm -rf " + listed_converted)
    os.system("mkdir -p " + listed_converted)
else:
    os.system("mkdir -p " + listed_converted)


def convert(file_dir, video_format):
    for root, dirs, files in os.walk(file_dir):
        num = 1
        for video in files:
            ori = os.path.join(to_be_converted, video)
            new_file_name = os.path.join(listed_converted, str(num) + '.' + str(video_format))
            num = num + 1

            if(str(video[-3:]) == video_format):
                os.system("ffmpeg -i " + ori + " -c:v copy -c:a aac " + converted + str(num) + '.' + str(video_format))
                os.system("ffmpeg -i " + ori + " -c:v copy -c:a aac " + new_file_name)
            else:
                print(num)
                # subprocess.call("ffmpeg -i " + ori + ' ' + new_file_name)
                # subprocess.call("cp " + new_file_name + ' ' + converted + '/' + str(video[:-3]) + 'mp4')
                os.system("ffmpeg -i " + ori + ' ' + new_file_name)

                os.system("cp " + new_file_name + ' ' + converted + '/' + str(video[:-3]) + 'mp4')
    print("====================")
    print("CONVERT FINISHED!!!!")
    print("====================")

    
convert(to_be_converted, 'mp4')
#get_file("/home/zhenhao/Documents/Projects/BorderInvading/video_datasets/to_be_converted")