import os
import shutil


# 针对训练集
def make_train_file():
    count = 1
    with open(r'/home/toky/Projects/af_SFMlearner_modified/splits/transcolon/train_files_ORIGIN.txt', 'a',
              encoding='utf-8') as f:
        for folder in range(7, 15):
            alllist = os.listdir(
                u"/home/toky/Datasets/colon_dataset_virtual/train_dataset/scence" + str(
                    folder) + "/photo/")  # 组装scence文件夹的名字
            max_index = len(alllist) - 2
            for i in alllist:
                if count >= max_index:
                    break
                else:
                    text = 'train_dataset/scence' + str(folder) + '\t' + str(count) + '\t' + "l" + '\n'
                    f.write(text)
                    count += 1
            count = 1


# 针对验证集
def make_validate_file():
    count = 1
    with open(r'/home/toky/Projects/af_SFMlearner_modified/splits/transcolon/train_files_ORIGIN.txt', 'a',
              encoding='utf-8') as f:
        for folder in range(7, 15):
            alllist = os.listdir(
                u"/home/toky/Datasets/colon_dataset_virtual/train_dataset/scence" + str(
                    folder) + "/photo/")  # 组装scence文件夹的名字
            max_index = len(alllist) - 2
            for i in alllist:
                if count >= max_index:
                    break
                else:
                    text = 'train_dataset/scence' + str(folder) + '\t' + str(count) + '\t' + "l" + '\n'
                    f.write(text)
                    count += 1
            count = 1


# 针对测试集
def make_test_file():
    count = 1
    with open(r'E:\Toky\af-SfMLearner_modified\splits\transcolon\val_files.txt', 'a',
              encoding='utf-8') as f:
        for folder in range(12, 15):
            # /home/toky/Datasets/colon_dataset_virtual/test_dataset/test
            alllist = os.listdir(
                u"I:/dataset/endo_dataset/validation_dataset/validate" + str(
                    folder) + "/photo/")  # 组装scence文件夹的名字
            max_index = len(alllist) - 2
            for i in alllist:
                if count >= max_index:
                    break
                else:
                    text = 'validation_dataset/validate' + str(folder) + '\t' + str(count) + '\t' + "l" + '\n'
                    f.write(text)
                    count += 1
            count = 1


if __name__ == '__main__':
    make_test_file()
    # 批量复制一个文件到多个文件夹下
    # alllist = os.listdir(u"E:\\Toky\\cam\\")
    # for folder in range(68, 151):
    #     for i in alllist:
    #         aa, bb = i.split(".")
    #         oldname = u"E:\\Toky\\cam\\" + aa + "." + bb
    #         newname = u"E:\\Toky\\dataSet\\tokydataset\\train_dataset\\scence" + str(folder) + "\\" + aa + "." + bb
    #         shutil.copyfile(oldname, newname)

    # 批量遍历一个文件夹下的所有文件，并写入到一个text文件中
