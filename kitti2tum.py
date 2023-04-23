# midified from https://github.com/anecjong/kitti_to_tum_format/blob/main/kitti_2_tum.py
from scipy.spatial.transform import Rotation
import numpy as np


def kitti2tum(kitti_pose_list):
    kitti_time_list = range(0, len(kitti_pose_list), 1)
    kitti_pose_list.sort()
    # kitti_time_list.sort()
    results_dict = {}
    file_contents = []

    for i in range(len(kitti_time_list)):
        # if kitti_pose_list[i].split(split_dir)[-1].split(".")[0] != \
        #         kitti_time_list[i].split(split_dir)[-1].split(".")[0]:
        #     print("check file names!")
        #     print(kitti_time_list[i])
        #     print(kitti_pose_list[i])
        #     return 1
        if type(kitti_pose_list[i]) is str:
            kitti_pose_list[i] = kitti_pose_list[i].split()
        lines_se3 = np.asarray(kitti_pose_list[i], dtype=float)

        lines_times = kitti_time_list[i]

        # for i, se3 in enumerate(lines_se3[:]):
        # se3 = list(map(float, se3.split()))
        rotation_matrix = [lines_se3[0:3], lines_se3[4:7], lines_se3[8:11]]
        r = Rotation.from_matrix(rotation_matrix)
        temp = [lines_se3[x] for x in [3, 7, 11]] + list(np.round(r.as_quat(), 6))
        time_stamp = float(lines_times)
        results_dict.update({time_stamp: temp})
        # file_contents.append(temp)
    return results_dict


if __name__ == "__main__":
    # test
    with open(
            r"E:\Toky\sc_depth_pl_modified\Swin_Depth_Pose_Net\.txt",
            "r") as f:
        pose = f.readlines()
    kitti2tum(pose)
