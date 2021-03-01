import json
import os

file_dir = "D:/YW_최종/yw_moblie_end"
os.chdir(file_dir)

label_part = ['전면', '좌측전면', '우측전면', '좌측면', '우측면', '후면', '좌측후면', '우측후면', '좌측전방타이어', '좌측후방타이어', '우측전방타이어', '우측후방타이어', '구분불가타이어', '실내', '계기판', '기울어진좌측면', '기울어진우측면', '사용불가좌측전방타이어', '사용불가좌측후방타이어', '사용불가우측전방타이어', '사용불가우측후방타이어', '사용불가구분불가타이어']
label_qual = ['좋음', '빛번짐', '흔들림']

all_file = os.listdir()
json_files = []
datas = []

for file in all_file:
    fname, ext = os.path.splitext(file)
    if ext == ".json":
        json_files.append(file)

for json_file in json_files:
    with open(json_file) as json_data:
        datas.append(json.load(json_data))

json_list = []
for data in datas:
    part_vehicle_string = ""
    image_qual_string = ""
    for shape in data["shapes"]:
        if shape["points"] == [[0.0, 0.0]] or shape["points"] == [[0, 0], [0, 0]]:
            part_vehicle_string = shape["label"]
        elif shape["points"] == [[1.0, 1.0]] or shape["points"] == [[1, 1], [1, 1]]:
            image_qual_string = shape["label"]
    for i in label_part:
        if part_vehicle_string == i:
            part_vehicle_string = label_part.index(i) + 1
    for i in label_qual:
        if image_qual_string == i:
            image_qual_string = label_qual.index(i) + 1

    file_data = {

    }
    file_data["image_id"] = data["imagePath"]
    file_data["part_vehicle"] = part_vehicle_string
    file_data["image_qual"] = image_qual_string
    file_data["damage"] = None
    file_data["type_damage"] = None
    file_data["bbox"] =None

    json_list.append(file_data)


with open("yw_moblie.json", "w", encoding="utf-8") as make_file:
    json.dump(json_list, make_file, ensure_ascii=False, indent="\t")
