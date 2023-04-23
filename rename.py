# -*- coding: utf-8 -*-
import os


def rename():
    a = 0
    for file in sorted_filenames:
        if a < 10:
            new_name = "000" + str(a) + ext_name
        elif a < 100:
            new_name = "00" + str(a) + ext_name
        elif a < 1000:
            new_name = "0" + str(a) + ext_name
        elif a < 10000:
            new_name = "" + str(a) + ext_name
        # os.rename(os.path.join(path, file), os.path.join(path, new_name))
        os.rename(os.path.join(path, file), os.path.join(path, new_name))
        a += 1


def mysort(path):
    filelists = os.listdir(path)
    sort_num_first = []
    for file in filelists:
        f = file.split(".")[0]
        g = f.split("_")[2]
        # sort_num_first.append(int(file.split(".")[0]))  # 根据 _ 分割，然后根据空格分割，转化为数字类型
        sort_num_first.append(int(g))
        sort_num_first.sort()
    sorted_file = []
    for sort_num in sort_num_first:
        for file in filelists:
            if str(sort_num) == file.split(".")[0]:
                sorted_file.append(file)
    return sorted_file


def depth_sort(path):
    # 针对形如 aov_image_0500 格式的深度图片
    filelists = os.listdir(path)
    sort_num_first = []
    for file in filelists:
        f = file.split(".")[0]
        g = f.split("_")[2]
        # sort_num_first.append(int(file.split(".")[0]))  # 根据 _ 分割，然后根据空格分割，转化为数字类型
        sort_num_first.append(int(g))
        sort_num_first.sort()
    sorted_file = []
    for sort_num in sort_num_first:
        for file in filelists:
            if sort_num == int(file.split(".")[0].split("_")[2]):
                sorted_file.append(file)
    return sorted_file


def depth_sort_endo(path):
    # 针对形如 frame_000044.jpg 格式的深度图片
    filelists = os.listdir(path)
    sort_num_first = []
    for file in filelists:
        f = file.split(".")[0]
        g = f.split("_")[1]
        # sort_num_first.append(int(file.split(".")[0]))  # 根据 _ 分割，然后根据空格分割，转化为数字类型
        sort_num_first.append(int(g))
        sort_num_first.sort()
    sorted_file = []
    for sort_num in sort_num_first:
        for file in filelists:
            if sort_num == int(file.split(".")[0].split("_")[1]):
                sorted_file.append(file)
    return sorted_file


def get_filename(file_dir):
    filename = None
    for root, dirs, files in os.walk(file_dir):
        # print(root) #当前目录路径
        # print(dirs) #当前路径下所有子目录
        # print(files) #当前路径下所有非目录子文件
        filename = files
    return filename


if __name__ == '__main__':
    ext_name = ".jpg"
    # for foler in range(12, 13):
    #     path = r'/home/toky/Datasets/colon_dataset_virtual/test_dataset/test' + str(foler) + '/depth'
    #     # sorted_filenames = depth_sort_endo(path)
    #     sorted_filenames = os.listdir(path)  # 不用排序的，以数字开头的
    #     rename()

    # sorted_filenames = depth_sort_endo(path)
    # sorted_filenames = os.listdir(path)  # 不用排序的，以数字开头的
    # rename()

    # 2023年4月5日
    with open(r'C:\Users\DELL\Desktop\Phantom\0408phantom-4\jpg2\images.txt', encoding='utf-8') as file:
        ori_filenames = file.readlines()
    ori_filenames = [i.rstrip() for i in ori_filenames]

    with open(r'C:\Users\DELL\Desktop\Phantom\0408phantom-4\depth\images.txt', encoding='utf-8') as file:
        sorted_filenames = file.readlines()
    sorted_filenames = [i.rstrip() for i in sorted_filenames]

    ori_path = r'C:\Users\DELL\Desktop\Phantom\0408phantom-4\jpg2/'
    new_path = r'C:\Users\DELL\Desktop\Phantom\0408phantom-4\depth/'
    for ori_file, new_file in zip(ori_filenames, sorted_filenames):
        os.rename(os.path.join(new_path, new_file), os.path.join(new_path, ori_file))
