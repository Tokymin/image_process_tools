import cv2
import numpy as np
import glob
import os


# 其它格式的图片也可以
def image2video():
    img_array = []
    for filename in glob.glob(
            'F:/Toky/Dataset/Endo_colon_unity/test_for_point_feature/photo3/test_feature_arrowLine/*.jpg'):
        img = cv2.imread(filename)
        height, width, layers = img.shape
        size = (width, height)
        img_array.append(img)

    # avi：视频类型，mp4也可以
    # cv2.VideoWriter_fourcc(*'DIVX')：编码格式
    # 5：视频帧率
    # size:视频中图片大小
    out = cv2.VideoWriter('I:/466350/Documents/谭敏/申请博士/面试考核准备资料/project-all.avi',
                          cv2.VideoWriter_fourcc(*'DIVX'),
                          5, size)

    for i in range(len(img_array)):
        out.write(img_array[i])
    out.release()


if __name__ == '__main__':
    image2video()
