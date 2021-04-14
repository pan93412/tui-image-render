'''
To run, you should download the Never Gonna Give You Up video
from YouTube, and extract to JPEG format with this command:

    $ ffmpeg -i VIDEO_NAME frames/frame%d.jpg
'''

from PIL import Image
from tui.processors import generate_frame, GenerateFrameConfiguration
from tui.renders.Terminal import Terminal
from multiprocessing import Pool

def open_and_generate_frame(i: int):
    # print(f"processing: {i}")
    img = Image.open(f"frames/frame{i}.jpg")
    frame = generate_frame(img, GenerateFrameConfiguration())
    
    return frame

if __name__ == '__main__':
    terminal = Terminal()

    with Pool(processes=16) as pool:
        res = pool.imap(open_and_generate_frame, range(1, 5301+1))
        
        while True:
            try:
                terminal.render_frame(next(res))
            except (StopIteration):
                break  # Video ended.

    print("All frames are played.  STOP.")
    