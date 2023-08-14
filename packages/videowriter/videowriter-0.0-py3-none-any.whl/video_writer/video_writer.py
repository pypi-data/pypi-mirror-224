import cv2

class VideoWriterWrapper:
    def __init__(self, filename,  fps, frame_size):
        code = None
        if filename.endswith(".avi"):
            code = "XVID"
        if filename.endswith(".mp4"):
            code = 'MPEG'
        if filename.endswith(".h265"):
            code = "HEVC"
        self.writer = cv2.VideoWriter(filename, cv2.VideoWriter_fourcc(*f'{code}'), fps, frame_size)

    def write_frame(self, frame):
        self.writer.write(frame)

    def release(self):
        self.writer.release()