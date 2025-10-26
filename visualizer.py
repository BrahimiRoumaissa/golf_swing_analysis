import cv2
import numpy as np

# ...existing code...

def draw_keypoints(img, keypoints, labels=None, color=(0,255,0)):
    for i, kp in enumerate(keypoints):
        if kp is None:
            continue
        x,y = int(kp[0]), int(kp[1])
        cv2.circle(img, (x,y), 5, color, -1)
        if labels:
            cv2.putText(img, labels[i], (x+5,y-5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 1)
    return img


def draw_boxes(img, boxes, classes=None):
    for i, b in enumerate(boxes):
        x1,y1,x2,y2 = [int(v) for v in b]
        cv2.rectangle(img, (x1,y1), (x2,y2), (0,255,0), 2)
        if classes:
            cv2.putText(img, classes[i], (x1,y1-10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,255,0), 2)
    return img


def annotate_frame(img, detections, metrics=None):
    # detections: dict with 'keypoints' or 'boxes'
    if 'keypoints' in detections:
        draw_keypoints(img, detections['keypoints'], detections.get('labels'))
    if 'boxes' in detections:
        draw_boxes(img, detections['boxes'], detections.get('labels'))
    if metrics:
        y = 20
        for k,v in metrics.items():
            cv2.putText(img, f"{k}: {v:.2f}", (10,y), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,0,255), 2)
            y += 20
    return img
