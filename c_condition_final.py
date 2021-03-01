import os
import json

main_dir = "D:/프로젝트 데이터 완료/콘스탄트/유분도_염증도/데이터"

os.chdir(main_dir)

make_data = {}

for file in os.listdir():
    with open(file, "r", encoding="utf-8") as json_file:
        data = json.load(json_file)
    make_data["{}.jpg".format(file.split(".")[0])] = data

print(len(make_data))

# with open("D:/프로젝트 데이터 완료/콘스탄트/condition_final.json", "w", encoding="utf-8") as make_file:
#     json.dump(make_data, make_file, ensure_ascii=False, indent=4)