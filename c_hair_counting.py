import os, json, math

currentFolderPath = "./"
distance = 20

# 현재 폴더 패스에서 모든 .json file의 이름을 가져온다.
def getAllJsonFilename():
  return list(filter(lambda x: x[-5:] == ".json" ,os.listdir(currentFolderPath)))

# json read
def readJson(filename):
  with open(filename, "r", encoding="utf-8") as jsonFile:
    return json.load(jsonFile)

def isWithinRange(node1, node2, distance):
  x = node1[0] - node2[0]
  y = node1[1] - node2[1]
  return math.sqrt((x ** 2) + (y ** 2)) <= distance

# 모발 카운트 process
def process(dataList, distance):
  size = len(dataList)
  for i in range(size):
    count = 0
    candidate = dataList[i]["points"][0]
    for j in range(size):
      if i == j:
        continue
      control = dataList[j]["points"][0]
      if isWithinRange(candidate, control, distance):
        count += 1
    dataList[i]["near_count"] = count

def save(filename, data):
  with open(filename[:-5] + "_add_count.json", "w", encoding = "utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
    f.close()



if __name__ == "__main__":
  for filename in getAllJsonFilename():
    data = readJson(filename)
    process(data['shapes'], distance)
    save(filename, data)



