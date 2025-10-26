import cv2
import os
from tqdm import tqdm

# ...existing code...

def extract_frames(video_path, out_dir, fps_ratio=1):
    os.makedirs(out_dir, exist_ok=True)
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        raise IOError(f"Cannot open video {video_path}")

    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    fps = cap.get(cv2.CAP_PROP_FPS) or 30
    step = max(1, int(fps / fps_ratio))

    idx = 0
    pbar = tqdm(total=total_frames, desc="Extracting frames")
    saved = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        if idx % step == 0:
            frame_path = os.path.join(out_dir, f"frame_{saved:06d}.jpg")
            cv2.imwrite(frame_path, frame)
            saved += 1
        idx += 1
        pbar.update(1)
    cap.release()
    pbar.close()
    return saved

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--video', type=str, required=True, help='Path to input video')
    parser.add_argument('--out', type=str, default='data/frames', help='Output frames directory')
    parser.add_argument('--fps_ratio', type=float, default=1.0, help='How many frames per second to keep (1 = full fps)')
    args = parser.parse_args()

    print('Extracting frames...')
    n = extract_frames(args.video, args.out, args.fps_ratio)
    print(f'Extracted {n} frames to {args.out}')
