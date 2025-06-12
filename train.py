

import os
import torch
from ultralytics import YOLO
# device = torch.device('gpu')
import os
os.environ['KMP_DUPLICATE_LIB_OK']='TRUE'


if __name__ == '__main__':
    model = YOLO('./ultralytics/cfg/models/v8/yolov8-C2f-ScConv.yaml')
    # result = model.train(data = 'data2.yaml', epochs=100, imgsz=416,batch = 4)




    result = model.train(data = 'data3.yaml', epochs=100, imgsz=640,batch=4)
