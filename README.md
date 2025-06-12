# Improvement of garbage detection algorithm based on yolov8
## Methods
Deformable Convolutional Networks(DCN)  
ShuffleAttention(SA)  
Spatial and Channel reconstruction Convolution(SCConv)   

## Data sources  
dataset1:http://123.56.14.89:8008/wfdownload/  
dataset2:https://pan.baidu.com/s/1nhzDgXyu6IKPNrrjOw883Q?pwd=54um  
dataset3:https://universe.roboflow.com/tamkang/marine-debris-yolo/Dataset/  

## Improve code path
 ./ultralytics/nn/modules/block.py

## Configuration file  
./ultralytics/cfg/models/v8  

## Environment
Python 3.8.10  
Torch 2.0.0  
Torchvision 0.15.1  
Torchaudio 2.0.1  
CUDA 11.8  
