import streamlit as st
import cv2
import os
import tempfile
from yolo_detector import YoloDetector
from visualizer import annotate_frame

st.set_page_config(page_title='Golf Swing Analysis', layout='wide')
st.title('Golf Swing Analysis')

# Ensure directories exist
os.makedirs('data/videos', exist_ok=True)
os.makedirs('data/results', exist_ok=True)

# Sidebar: single refresh button (replaces previous video selection UI)
uploaded = st.file_uploader('Upload a raw golf swing video (saved to data/videos)', type=['mp4', 'mov', 'avi', 'mkv'])
if st.sidebar.button('Refresh video lists'):
    # Streamlit automatically reruns on widget interaction; explicit experimental_rerun is unavailable in some versions
    st.sidebar.success('Video lists refreshed')

def save_uploaded(uploaded_file):
    os.makedirs('data/videos', exist_ok=True)
    path = os.path.join('data', 'videos', uploaded_file.name)
    with open(path, 'wb') as f:
        f.write(uploaded_file.getbuffer())
    return path

if uploaded is not None:
    video_path = save_uploaded(uploaded)
    st.sidebar.success(f'Uploaded raw video: {os.path.basename(video_path)}')
else:
    video_path = None

# Downloads & Previews removed per user request

# Main preview area — show latest annotated result if available, else uploaded raw video
st.header('Video Preview')
results_list = sorted([f for f in os.listdir('data/results') if f.lower().endswith(('.mp4', '.mov', '.avi', '.mkv'))])
if results_list:
    latest = results_list[-1]
    preview_path = os.path.join('data/results', latest)
    if os.path.exists(preview_path):
        st.video(preview_path)
        st.write(f'Previewing latest annotated result: {latest}')
    else:
        st.error('Latest annotated file does not exist')
elif uploaded is not None:
    uploaded_path = os.path.join('data/videos', uploaded.name)
    if os.path.exists(uploaded_path):
        st.video(uploaded_path)
        st.write(f'Previewing uploaded raw video: {uploaded.name}')
    else:
        st.error('Uploaded video not found')
else:
    st.info('No annotated results found. Upload a raw video to add to the list.')

# End of app
