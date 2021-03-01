import os
import json
import datetime

start = datetime.datetime.now()

main_dir = "D:/프로젝트 데이터 완료/콘스탄트/데이터_1"

os.chdir(main_dir)
all_file_list = os.listdir()
json_list = []
datas = []
constant1_list = []
constant2_list = []
constant3_list = []
constant4_list = []

all_point = 0
constant1_point = 0
constant2_point = 0
constant3_point = 0
constant4_point = 0

for file in all_file_list:
    if file[-4:] == "json":
        json_list.append(file)

for i in json_list:
    if i[:9] == "constant1":
        constant1_list.append(i)
    elif i[:9] == "constant2":
        constant2_list.append(i)
    elif i[:9] == "constant3":
        constant3_list.append(i)
    elif i[:9] == "constant4":
        constant4_list.append(i)
    else:
        print(i)

for json_file in json_list:
    with open(json_file, "r") as json_data:
        data = json.load(json_data)
        datas.append(data)
        all_point += len(data["shapes"])
for constant1_file in constant1_list:
    with open(constant1_file, "r") as json_data:
        data = json.load(json_data)
        datas.append(data)
        constant1_point += len(data["shapes"])
for constant2_file in constant2_list:
    with open(constant2_file, "r") as json_data:
        data = json.load(json_data)
        datas.append(data)
        constant2_point += len(data["shapes"])
for constant3_file in constant3_list:
    with open(constant3_file, "r") as json_data:
        data = json.load(json_data)
        datas.append(data)
        constant3_point += len(data["shapes"])
for constant4_file in constant4_list:
    with open(constant4_file, "r") as json_data:
        data = json.load(json_data)
        datas.append(data)
        constant4_point += len(data["shapes"])

print("all_point: ", all_point)
print("constant1_point: ", constant1_point)
print("constant2_point: ", constant2_point)
print("constant3_point: ", constant3_point)
print("constant4_point: ", constant4_point)

end = datetime.datetime.now()
print(start - end)
