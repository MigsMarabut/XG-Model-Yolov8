import os
import subprocess

# Clone YOLOv9 repository
if not os.path.exists('yolov9'):
    subprocess.run(['git', 'clone', 'https://github.com/WongKinYiu/yolov9'])

# Change directory to yolov9
os.chdir('yolov9')

# Install dependencies
subprocess.run(['pip', 'install', '-r', 'requirements.txt'])

# Download YOLOv9 weights
if not os.path.exists('yolov9-c.pt'):
    import urllib.request
    urllib.request.urlretrieve('https://github.com/WongKinYiu/yolov9/releases/download/v0.1/yolov9-c.pt', 'yolov9-c.pt')
