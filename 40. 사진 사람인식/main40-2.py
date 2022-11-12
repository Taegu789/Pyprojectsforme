import torch
from glob import glob

img_path = r'40. 사진 사람인식\checker'

img_list = glob(img_path + "\*.jpg")

model = torch.hub.load('ultralytics/yolov5','yolov5s')

for img_path in img_list :
    results = model(img_path)
    print(img_path)
    results.save(save_dir=r"C:\Users\user\Downloads\Pyprojectsforme\40. 사진 사람인식\찰칵")
    for pred in results.pred[0]:
        tag = results.names[int(pred[-1])]
        print(tag)