# 读取json文件内容,返回字典格式
import json
import os
import numpy as np

file_path = "H:\\dataset\\SCARED\\dataset_2\\keyframe_1\\data\\frame_data"
poses = []
for file in os.listdir(file_path):
    with open(file_path + "\\" + file, 'r', encoding='utf8')as fp:
        json_data = json.load(fp)
        # print('这是文件中的json数据：', json_data)
        # print('这是读取到文件数据的数据类型：', type(json_data))
        # print(json_data['camera-pose'])
        j = np.asarray(json_data['camera-pose'])[0:3]
        p = j.reshape(-1, 12)
        poses.append(p)
poses = np.concatenate(poses, axis=0)
np.savetxt("H:\\dataset\\SCARED\\dataset_2\\keyframe_1\\data" + "\\gt_pose_kitti.txt", poses,
           delimiter=' ', fmt='%1.8e')
