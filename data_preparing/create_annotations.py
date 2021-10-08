import sys
sys.path.append("..")

import json
import os
import cv2
from utils.data_utils import get_mp4_length, translate_seconds_to_hms, num2str, num2second


project_dir = '/home/zhenhao/Documents/Projects/BorderInvading/'
# listed_dataset_dir = 'video_datasets/listed_converted'
listed_dataset_dir = 'video_datasets/test'
save_dir = 'annotations/test'

listed_converted = os.path.join(project_dir, listed_dataset_dir)
annotation_save_path = os.path.join(project_dir, save_dir)

class Annotation():
    def __init__(self):
        self.exception_template = {
            "start": "00:00:00",
            "end": "00:00:00",
            "type": "human_crossing",
        }

        self.annotation_template = {
            "filename": "default_file_name",
            "duration": 0,
            "exceptions": [],
        }

        self.annotation = self.annotation_template.copy()
        self.exception = self.exception_template.copy()

    def change_exception(self):
        self.exception['start'] = self.exception_start
        self.exception['end'] = self.exception_end
        self.exception['type'] = self.exception_type

    def change_annotation(self, root_path, video_name):
        video_path = os.path.join(root_path, video_name)
        self.duration = get_mp4_length(video_path)
        print(video_path)
        print(root_path)
        print(self.duration)
        self.filename = video_name

        self.annotation['filename'] = self.filename
        self.annotation['duration'] = self.duration
        while (1):
            self.exception_start = input("Input the start time of an exception:\n")
            self.exception_end = input("Input the end time of an exception:\n")
            self.exception_type = input("Input the type of an exception:\n")
            self.change_exception()
            self.annotation['exceptions'].append(self.exception)

            go_on = input("Want to continue?\n")
            if(go_on == "yes" or go_on == "Yes"):
                continue
            else:
                break

    def save_to_json(self, save_path = annotation_save_path):
        annotaation_json = json.dumps(self.annotation)
        print("Start writting json")
        json_path = os.path.join(annotation_save_path, str(self.filename[:-4]) + '.json')
        #print(json_path)
        with open(json_path, 'w') as json_file:
            json.dump(annotaation_json, json_file, indent=4)
            print("write json file success!")


for root, dirs, files in os.walk(listed_converted):
    num = 1
    for video in files:
        print("Start to annotate for %s." %video)
        each_annotation = Annotation()
        video_name = video
        each_annotation.change_annotation(listed_converted, video_name)
        each_annotation.save_to_json()

    print("===================")
    print("Annotations complete!")
    print("===================")