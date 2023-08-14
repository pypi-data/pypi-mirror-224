import cv2

class VideoWriterWrapper:
    def __init__(self, filename, code, fps, frame_size):
        self.writer = cv2.VideoWriter(filename, cv2.VideoWriter_fourcc(*f'{code}'), fps, frame_size)

    def write_frame(self, frame):
        self.writer.write(frame)

    def release(self):
        self.writer.release()