import json

with open("/home/zhenhao/Documents/Projects/BorderInvading/annotations/test/3.json", 'r') as load_f:
    load_dict = json.load(load_f)
    print(load_dict)