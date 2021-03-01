import csv
import time
import requests
import re
import json
import datetime

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

start = time.time()

now = datetime.datetime.now()

URL = 'https://tumblbug.com/discover'
file_dir = "C:/python_result"
# file_name = 'tumblbug_crawling_{}_{}'.format(URL.split("=")[1], now.strftime("%y_%m_%d"))
file_name = 'tumblbug_crawlling_all_{}'.format(now.strftime("%y_%m_%d"))

driver = webdriver.Chrome(executable_path='chromedriver')
driver.get(url=URL)

time.sleep(1)

SCROLL_PAUSE_SEC = 0.5

last_height = driver.execute_script("return document.body.scrollHeight")  # 스크롤 높이 가져옴
elem = driver.find_element_by_tag_name("body")
counter = 10

while True:
    elem.send_keys(Keys.PAGE_DOWN)  # page_down 키 입력
    time.sleep(SCROLL_PAUSE_SEC)
    new_height = driver.execute_script("return document.body.scrollHeight")      # 스크롤 다운 후 스크롤 높이 다시 가져옴
    if new_height == last_height:
        counter -= 1
        if counter == 0:
            break
    else:
        counter = 10
    last_height = new_height

provider_elems = driver.find_elements_by_xpath("//div[@class='ProjectCard__Card-opxl0a-5 euKJsj link-wrapper']")

print("pagedown 끝")

url_list = []

for post in provider_elems:
    url = post.find_element_by_xpath("./dl/dt/a").get_attribute("href")
    url_list.append(url)

driver.close()
print("총 {}개의 url이 수집되었습니다. \n".format(len(url_list)))

data_list = []
error_urls = []
for idx, url in enumerate(url_list):
    try:
        page_source = requests.get(url).text
        matched = re.search(r'window.MOBX_STATE = (.*?);', page_source, re.DOTALL)

        json_string = matched.group(1)
        course_list = json.loads(json_string)

        category = course_list["projectStore"]["projects"]["{}".format(list(course_list["projectStore"]["projects"].keys())[0])]["category"]
        title = course_list["projectStore"]["projects"]["{}".format(list(course_list["projectStore"]["projects"].keys())[0])]["title"]
        state = course_list["projectStore"]["projects"]["{}".format(list(course_list["projectStore"]["projects"].keys())[0])]["state"]
        funding_amount = course_list["projectStore"]["projects"]["{}".format(list(course_list["projectStore"]["projects"].keys())[0])]["fundedAmount"]
        funding_goal = course_list["projectStore"]["projects"]["{}".format(list(course_list["projectStore"]["projects"].keys())[0])]["fundingGoal"]
        funding_start_date = course_list["projectStore"]["projects"]["{}".format(list(course_list["projectStore"]["projects"].keys())[0])]["fundingStart"].split("T")[0]
        funding_end_date = course_list["projectStore"]["projects"]["{}".format(list(course_list["projectStore"]["projects"].keys())[0])]["fundingDeadline"].split("T")[0]
        support_amount = course_list["projectStore"]["projects"]["{}".format(list(course_list["projectStore"]["projects"].keys())[0])]["pledgesCount"]
        creator = course_list["projectStore"]["projects"]["{}".format(list(course_list["projectStore"]["projects"].keys())[0])]["creatorName"]
        tags = course_list["projectStore"]["projects"]["{}".format(list(course_list["projectStore"]["projects"].keys())[0])]["tags"]
        funding_url = course_list["projectStore"]["projects"]["{}".format(list(course_list["projectStore"]["projects"].keys())[0])]["url"]

        funding = [category, title, state, funding_amount, funding_goal, funding_start_date, funding_end_date, support_amount, creator, tags, funding_url]
        data_list.append(funding)
    except Exception as exception:
        error_urls.append(url)
        print(url, " / ", type(exception))

print("총 {}개의 오류가 발생했습니다.".format(len(error_urls)))

with open('{}/{}_error.csv'.format(file_dir, file_name), "w", encoding="utf-8", newline='') as csv_file_error:
    writer_e = csv.writer(csv_file_error)
    writer_e.writerow(["category", "title", "state", "fundedAmount", "fundingGoal", "fundingStart", "fundingDeadline", "pledgesCount", "creatorName", "tags", "url"])
    for error_url in error_urls:
        writer_e.writerow(["", "", "", "", "", "", "", "", "", "", error_url])

with open('{}/{}.csv'.format(file_dir, file_name), "w", encoding="utf-8", newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(["분류", "제목", "상태", "펀딩금액", "목표금액", "런칭날짜", "마감날짜", "후원자수", "창작자", "태그", "url"])
    for datas in data_list:
        writer.writerow(datas)

print("코딩 끝! 걸린시간은 {}초 입니다!".format(time.time()-start))