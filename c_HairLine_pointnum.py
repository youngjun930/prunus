import os
import json

main_dir = "D:/프로젝트 데이터/콘스탄트/검수_수정용"

os.chdir(main_dir)
all_file_list = os.listdir()
json_list = []
datas = []

all_point = 0

for file in all_file_list:
    if file[-4:] == "json":
        json_list.append(file)

for json_file in json_list:
    with open(json_file, "r") as json_data:
        data = json.load(json_data)
        datas.append(data)
        for point in data["shapes"]:
            if len(point["points"]) != 4:
                print(json_file, "/", point["label"], "/", len(point["points"]))