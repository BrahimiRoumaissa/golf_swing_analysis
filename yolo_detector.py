import os
from ultralytics import YOLO
import cv2
import numpy as np

# ...existing code...

class YoloDetector:
    def __init__(self, weights_path=None, device='cpu'):
        self.model = YOLO(weights_path or 'yolov8n.pt')

    def detect_frame(self, frame):
        # ultralytics returns results with boxes and keypoints when trained
        results = self.model(frame)
        detections = []
        for r in results:
            boxes = r.boxes.xyxy.cpu().numpy() if hasattr(r.boxes, 'xyxy') else []
            probs = r.boxes.conf.cpu().numpy() if hasattr(r.boxes, 'conf') else []
            cls = r.boxes.cls.cpu().numpy() if hasattr(r.boxes, 'cls') else []
            detections.append({'boxes': boxes, 'conf': probs, 'cls': cls})
        return detections

    def detect_frames(self, frames):
        return [self.detect_frame(f) for f in frames]

if __name__ == '__main__':
    # quick test
    img = cv2.imread('data/frames/frame_000000.jpg')
    d = YoloDetector()
    res = d.detect_frame(img)
    print(res)
