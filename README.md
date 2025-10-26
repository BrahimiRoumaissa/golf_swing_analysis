# Golf Swing Analysis System

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

A simple starter repository for a Golf Swing Analysis System using YOLO and OpenCV to process videos, extract frames, run detections, and visualize results.

## Features

- Frame extraction from videos (`python video_processor.py`)
- Object detection using YOLO (`yolo_detector.py` / `yolov8n.pt`)
- Analysis helpers (`analyzer.py`) and visualization (`visualizer.py`)
- Streamlit-based demo (`app.py`)

## Repository layout

- `data/`
  - `videos/` - place source videos here
  - `frames/` - extracted frames
  - `results/` - output images and reports
- `yolo_training/` - helper files and training dataset
- `yolov8n.pt` - example model (large binary — consider Git LFS)
- `video_processor.py`, `yolo_detector.py`, `analyzer.py`, `visualizer.py`, `app.py`

## Requirements

This project depends on common Python packages. Install them with:

PowerShell (Windows):

    pip install -r requirements.txt

(Consider using a virtual environment.)

## Usage

1. Add one or more video files to `data/videos/`.
2. Extract frames:

    python video_processor.py

3. Run detection / analysis pipeline (example):

    python app.py

4. Results will be placed under `data/results/`.

## Notes about large files

- Model weights such as `.pt` files and training `weights/` can be large. This repository's `.gitignore` excludes them by default. If you want to track model weights, use Git LFS (https://git-lfs.github.com/).

## Contributing

Contributions are welcome. See `CONTRIBUTING.md` for guidelines.

## License

This project is licensed under the MIT License - see the `LICENSE` file for details.
# golf_swing_analysis


