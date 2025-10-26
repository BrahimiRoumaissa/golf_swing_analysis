# Starter training script for YOLOv8 (ultralytics)
from ultralytics import YOLO
import argparse
import os

# ...existing code...

def train(cfg='yolo_training/dataset.yaml', epochs=50, imgsz=640, batch=8, weights=None):
    model = YOLO('yolov8n.pt' if weights is None else weights)
    model.train(data=cfg, epochs=epochs, imgsz=imgsz, batch=batch)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--data', default='yolo_training/dataset.yaml')
    parser.add_argument('--epochs', type=int, default=50)
    parser.add_argument('--imgsz', type=int, default=640)
    parser.add_argument('--batch', type=int, default=8)
    parser.add_argument('--weights', default=None)
    args = parser.parse_args()

    train(cfg=args.data, epochs=args.epochs, imgsz=args.imgsz, batch=args.batch, weights=args.weights)
