import cv2
import argparse
import os


def parse_args():
    """Parse input arguments"""
    parser = argparse.ArgumentParser(description='Process pic')
    parser.add_argument('--input', help='video to process', dest='input', default=None, type=str)
    parser.add_argument('--output', help='pic to store', dest='output', default=None, type=str)
    # default为间隔多少帧截取一张图片；我这里用10刚刚好！
    parser.add_argument('--skip_frame', dest='skip_frame', help='skip number of video', default=2, type=int)
    # input为输入视频的路径 ，output为输出存放图片的路径
    args = parser.parse_args(['--input', r'E:\Toky\rawData\01.0000000126336.10012.0003.09152900142.mp4', r'--output',
                              r'E:\Toky\dataSet\tokydataset\test_dataset\real\photo\\'])
    return args


def process_video(i_video, o_video, num):
    cap = cv2.VideoCapture(i_video)
    num_frame = cap.get(cv2.CAP_PROP_FRAME_COUNT)
    print(num_frame)
    expand_name = '.jpg'
    if not cap.isOpened():
        print("Please check the path.")
    cnt = 0
    count = 0
    # print(newdir)

    while count < num_frame:
        ret, frame = cap.read()
        cnt += 1
        #  计算frame数目
        if cnt % num == 0:
            count += 1
            newdir = os.path.join(o_video, str(count).zfill(6) + expand_name)
            # frame = frame[1024:2048, 0:1280]  # 裁剪一半,针对SCARED数据集
            frame = frame[124: 952, 794: 1755]  # 裁剪掉结肠视频帧中的黑色边框区域
            frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)
            cv2.imwrite(newdir, frame)
        if not ret:
            break


if __name__ == '__main__':
    args = parse_args()
    if not os.path.exists(args.output):
        os.makedirs(args.output)
    print('Called with args:')
    print(args)
    process_video(args.input, args.output, args.skip_frame)
