import os
import json

key_list =[139,140,141,142,143,144,145,303,304,305,306,307,308,294,295,296,297,298,299,300,301,200,201,202,203,204,205,206,286,207,208,209,283,210,211,285,212,213,287,214,215,284,216,217,218,219,1120,1121,1122,1136,1137,1138,1151,1133,1134,1135,1130,1131,1132,1127,1128,1129,1123,1124,1125,1126,1091,1092,1093,1094,1095,1096,1097,1098,1099,1100,1101,1102,1103,1104,1105,1106,1107,1108,1109,1110,1111,1112,1113,1114,1115,1226,1116,1117,1118,1119]
value_list = [1,2,3,4,5,6,7,1,2,3,4,5,6,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,1,2,3,1,2,3,1,2,3,4,1,2,3,1,2,3,4,1,2,3,1,2,3,1,2,3,1,2,3,4,1,2,3,4,5,1,2,3,1,2,3,4,1,2,3,4,1,2,1,2,1,2,3,4,5,6,1,2,3,4]

indexing = {}

while len(key_list) != 0:
    indexing["{}".format(key_list.pop())] = "{}".format(value_list.pop())

main_dir = "D:/프로젝트 데이터 완료/와들_완료"
final_dir = "D:/프로젝트 데이터 완료/waddle"


box_folder_list = ["테이블", "의자", "수납장", "옷장"]

category = {"테이블": 0, "의자": 1, "수납장": 2, "옷장": 3}

for box_folder in box_folder_list:
    os.chdir("{}/{}".format(main_dir, box_folder))
    box_file = os.listdir()
    for box in box_file:
        with open(box, "r", encoding="utf-8") as box_json_file:
            data = json.load(box_json_file)
            category_id = category["{}".format(box_folder)]
            counter = 0
            annotations = []
            for box_num in data["shapes"]:
                attributes = {}
                for key, val in box_num["label"].items():
                    attributes["{}".format(indexing["{}".format(key)])] = indexing["{}".format(val)]
                box_num["label"] = attributes
                counter += 1
                info = {}
                info["bbox_id"] = counter
                info["bbox"] = box_num["points"]
                info["attributes"] = box_num["label"]
                annotations.append(info)
            file_data = {}

            file_data["category_id"] = category_id
            file_data["annotations"] = annotations

            with open("{}/{}".format(final_dir, box), "w", encoding="utf-8") as make_file:
                json.dump(file_data, make_file, ensure_ascii=False, indent=4)

