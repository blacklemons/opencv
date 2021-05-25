import cv2
import numpy as np

class MyWindow():
    def __init__(self):
        super().__init__()
        self.ret = None
        self.frame = None
        self.blur_image = None
        self.title = "frame"
        self.cam_id = 0
        self.cap = 0
        #색상 필터
        self.yellow=1
        self.cobaltblue=0
        self.purple=0
        
    def show_camera(self):
        self.cap = cv2.VideoCapture(self.cam_id)
        if not self.cap.isOpened():
            raise FileNotFoundError()
        size = (640,480)
        while 1:
            ret, self.frame = self.cap.read()
            self.yello = 1
            b,g,r = cv2.split(self.frame)
            self.frame = cv2.merge((b,g,r)) # 왜 나누었다가 합친거지?
            if self.yellow == 1:
                self.frame[:, :, 0] = 0  # Y
            if self.purple == 1:
                self.frame[:, :, 1] = 0  # P
            if self.cobaltblue == 1:
                self.frame[:, :, 2] = 0  # C

            # 프레임 영상 크기 조절
            self.frame = cv2.resize(self.frame, size)

            # 이미지 출력
            cv2.imshow(self.title, self.frame)
            if cv2.waitKey(33) == 27:
                self.close_windows()

    def close_windows(self):
        cv2.destroyAllWindows('frame')


def main():
    editor = MyWindow()
    editor.show_camera()
    #editor.show()
    #app.exec_()

if __name__ == "__main__":
    main()