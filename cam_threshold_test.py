import cv2
import numpy as np

class MyWindow():
    def __init__(self):
        super().__init__()
        self.ret = None
        self.frame = None
        self.blur_image = None
        self.title = "frame"
        self.initial()

    def initial(self):
        self.cam_id = 0
        self.cap = 0
        self.gray = None
        self.edged = None
        self.image_copy = None
        self.title_copy = "copy"
        self.size = (640,480)
        
    def show_camera(self):
        self.cap = cv2.VideoCapture(self.cam_id)
        if not self.cap.isOpened():
            raise FileNotFoundError()
        while 1:
            ret, self.frame = self.cap.read()
            #ret, self.frame = cv2.threshold(self.frame, threshold, 255, thr_type)
            b,g,r = cv2.split(self.frame)
            self.frame = cv2.merge((b,g,r)) # 왜 나누었다가 합친거지?

            # 프레임 영상 크기 조절
            self.frame = cv2.resize(self.frame, self.size)

            self.threshold()
            
            # 이미지 출력
            cv2.imshow(self.title, self.frame)
            if cv2.waitKey(33) == 27:
                self.close_windows()

    def threshold(self):
        cv2.namedWindow("BINARY", cv2.WINDOW_NORMAL)
        ret, thr1 = cv2.threshold(self.frame, 127, 255, cv2.THRESH_BINARY)
        thr1 = cv2.resize(thr1, self.size)
        cv2.imshow("BINARY", thr1)

    def close_windows(self):
        cv2.destroyAllWindows('frame')


def main():
    editor = MyWindow()
    editor.show_camera()

if __name__ == "__main__":
    main()