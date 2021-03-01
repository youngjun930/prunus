import csv
import requests
import re
import json
import os

url_list = []
main_dir = "C:/python_result"
target_file = "tumblbug_crawling_game_error.csv"
result_dir = "{}/{}".format(main_dir, target_file.split(".")[0])

os.mkdir("{}/{}".format(main_dir, target_file.split(".")[0]))

with open("{}/{}".format(main_dir,target_file), "r", encoding="utf-8") as error_file:
    csv_data = csv.reader(error_file)
    next(csv_data)
    for i in csv_data:
        url_list.append(i[10])

for url in url_list:
    page_source = requests.get(url).text

    with open("{}/{}.txt".format(result_dir, url.split("com/")[1].split("?")[0]), "w", encoding="utf-8") as result_file:
        result_file.write(page_source)

