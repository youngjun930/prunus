import numpy as np
import cv2
import os

video_dir = "D:/프로젝트 데이터/한국축산데이터/동영상"  # 동영상 파일 저장 위치
image_dir = "D:/프로젝트 데이터/한국축산데이터/cut"    # 프레임단위로 잘린 이미지가 저장되는 위치

video_list = os.listdir(video_dir)


os.chdir(image_dir)

for video in video_list:
    paths = "{}/{}".format(video_dir, video)
    capture = cv2.VideoCapture(paths)
    print(paths)
    count = 1

    while capture.isOpened():
        ret, image = capture.read()
        print(capture.get(1))
        if ret:
            if int(capture.get(1)) % 10 == 0: # 자르는 단위 프레임 수
                print("saved frame number : " + str(int(capture.get(1))))
                cv2.imwrite("{}_frame_{}.jpg".format(video.split(".")[0], count), image)
                print("saved frame_{}.jpg".format(count))
                count += 1
            if capture.get(1) == capture.get(cv2.CAP_PROP_FRAME_COUNT):
                print("{} frame number : ".format(video) + str(int(capture.get(cv2.CAP_PROP_FRAME_COUNT))))
                print("video end")
                break
        else:
            print("flase")
            break
    capture.release()