import os
import json
from collections import OrderedDict
import shutil

target_dir = "D:/waddle_csv/box_2"
final_dir = ""
os.chdir(target_dir)


all_file_list = os.listdir()

image_list = []
json_list = []

for i in all_file_list:
    if i[-4:] == "json":
        json_list.append(i)
    elif i[-3:] == "jpg":
        image_list.append(i)

for i in json_list:
    with open("{}/{}".format(target_dir, i), "r", encoding="utf8") as json_data:
        data = json.load(json_data)
        bbox_id_num = len(data["shapes"])
        bbox_id_list = list(range(len(data["shapes"])))
        annotaions = []
        for j in bbox_id_list:
            l_x_point = data["shapes"][j]["points"][0][0]
            l_y_point = data["shapes"][j]["points"][0][1]
            r_x_point = data["shapes"][j]["points"][1][0]
            r_y_point = data["shapes"][j]["points"][1][1]
            bbox_id = j
            bbox = [l_x_point, l_y_point, r_x_point, r_y_point]
            annotaion = {"bbox_id":bbox_id, "bbox":bbox}
            annotaions.append(annotaion)
        group_data = OrderedDict()
        group_data["annotations"] = annotaions
        with open('{}'.format(i), 'w', encoding="utf-8") as make_file:
            json.dump(group_data, make_file, ensure_ascii=False, indent=2)



