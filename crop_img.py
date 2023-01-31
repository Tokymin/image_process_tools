from PIL import Image
import os


def rename(a):
    if a < 10:
        new_name = "000" + str(a) + ext_name
    elif a < 100:
        new_name = "00" + str(a) + ext_name
    elif a < 1000:
        new_name = "0" + str(a) + ext_name
    elif a < 10000:
        new_name = "" + str(a) + ext_name
    # os.rename(os.path.join(path, file), os.path.join(path, new_name))
    return new_name


def mysort(path):
    "形如ImagesName1"
    suffix = "jpg"
    filelists = os.listdir(path)
    sort_num_first = []
    for file in filelists:
        if file.split(".")[1] != suffix:
            continue
        f = file.split("Name")[1]
        g = f.split(".")[0]
        # sort_num_first.append(int(file.split(".")[0]))  # 根据 _ 分割，然后根据空格分割，转化为数字类型
        sort_num_first.append(int(g))
        sort_num_first.sort()
    sorted_file = []
    for sort_num in sort_num_first:
        for file in filelists:
            if file.split(".")[1] != suffix:
                continue
            t=file.split("Name")[1].split(".")[0]
            if str(sort_num) ==t:
                sorted_file.append(file)
    return sorted_file


if __name__ == '__main__':
    ext_name = ".jpg"
    # for foler in range(12, 13):
    #     path = r'/home/toky/Datasets/colon_dataset_virtual/test_dataset/test' + str(foler) + '/depth'
    #     # sorted_filenames = depth_sort_endo(path)
    #     sorted_filenames = os.listdir(path)  # 不用排序的，以数字开头的
    #     rename()
    path = r'F:\Toky\Dataset\体膜数据集\Colon Dataset\record02（backward slow）'
    # sorted_filenames = depth_sort_endo(path)
    sorted_filenames = mysort(path)  # 不用排序的，以数字开头的
    for i, file in zip(range(len(sorted_filenames)), sorted_filenames):
        img = Image.open(path + "\\" + file)
        # 图像打开之后用该对象去调用crop()方法即可裁剪图片了，这个方法需要传入四个参数，而这四个参数则分别表示了图像裁剪范围四个角。
        # 按照顺序来看就是左上角、右上角、左下角以及右下角，而这几个值对于的则分别为长度、宽度、宽度、长度，代码示例如下所示：
        # Image.crop(left, up, right, below)
        # left：与左边界的距离
        # up：与上边界的距离
        # right：还是与左边界的距离
        # below：还是与上边界的距离
        region = img.crop((150, 65, 520, 415))  # 注意这里的right 和below

        region.save('F:\Toky\Dataset\体膜数据集\Colon Dataset\processed\\part1_record02（backward slow）\image_{}'.format(rename(i)))
