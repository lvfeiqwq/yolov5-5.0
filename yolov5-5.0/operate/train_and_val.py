import os
import shutil


def process(source, src_path, tar_path, end):
    with open(src_path) as f:
        train_list = f.read().splitlines()
        print(train_list)
        print(len(train_list))
        for each in train_list:
            shutil.move(source + "\\" + each + end, tar_path)


if __name__ == '__main__':
    path_train = r'D:\Desktop\yolov5-5.0\yolov5-5.0\VOC2028\ImageSets\Main\train.txt'
    path_val = r'D:\Desktop\yolov5-5.0\yolov5-5.0\VOC2028\ImageSets\Main\val.txt'
    path_test = r'D:\Desktop\yolov5-5.0\yolov5-5.0\VOC2028\ImageSets\Main\test.txt'
    # 图片数据分类 训练+验证+测试
    source_img = r'D:\Desktop\yolov5-5.0\yolov5-5.0\VOC2028\JPEGImages'
    tar_train = r'D:\Desktop\yolov5-5.0\yolov5-5.0\VOC2028\images\train'
    tar_val =  r'D:\Desktop\yolov5-5.0\yolov5-5.0\VOC2028\images\val'
    tar_test = r'D:\Desktop\yolov5-5.0\yolov5-5.0\VOC2028\images\test'
    # process(source_img, path_train, tar_train, '.jpg')
    # process(source_img, path_val, tar_val, '.jpg')
    process(source_img, path_test, tar_test, '.jpg')
    # 标签分类
    # source_labels = r'D:\Desktop\yolov5-5.0\yolov5-5.0\VOC2028\txt_labels'
    # tar_train_labels = r'D:\Desktop\yolov5-5.0\yolov5-5.0\VOC2028\labels\train'
    # tar_val_labels = r'D:\Desktop\yolov5-5.0\yolov5-5.0\VOC2028\labels\val'
    # process(source_labels, path_train, tar_train_labels, '.txt', )
    # process(source_labels, path_val, tar_val_labels, '.txt', )

# def doc_rename(path_src, path_dst, begin_num):
#     for i in os.listdir(path_src):
#         # 获取原始文件名
#         doc_src = os.path.join(path_src, i)
#         # 重命名
#         doc_name = rename_format.format(begin_num, os.path.splitext(i)[-1])
#         # 确定目标路径
#         doc_dst = os.path.join(path_dst, doc_name)
#         begin_num += 1
#         os.rename(doc_src, doc_dst)
#
#
# # 运行函数
# doc_rename(path_src, path_dst, begin_num)
#
