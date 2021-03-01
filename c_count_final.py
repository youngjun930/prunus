import os
import json

main_dir = "D:/프로젝트 데이터 완료/콘스탄트/원본/add_count"
save_dir = "D:/프로젝트 데이터 완료/콘스탄트/count_final"

os.chdir(main_dir)

file_list = os.listdir()

for file in file_list:
    with open(file, "r", encoding="utf-8") as json_data:
        data = json.load(json_data)
    image_name = file[10:].split(".")[0][:-10] + ".jpg"
    make_data = {}
    datas = []

    for shapes in data["shapes"]:
        label = {}
        label["points"] = shapes["points"]
        label["near_count"] = shapes["near_count"]
        datas.append(label)
    make_data["{}".format(image_name)] = datas
    with open("{}/{}.json".format(save_dir, image_name.split(".")[0]), "w", encoding="utf-8") as make_file:
        json.dump(make_data, make_file, ensure_ascii=False, indent=4)


