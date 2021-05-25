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
        self.size2 = (320,240)
        
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
        if self.frame is None:
            return
        cv2.namedWindow("BINARY", cv2.WINDOW_NORMAL)
        cv2.namedWindow("BINARY_INV", cv2.WINDOW_NORMAL)
        cv2.namedWindow("TRUNC", cv2.WINDOW_NORMAL)
        cv2.namedWindow("TOZERO", cv2.WINDOW_NORMAL)
        cv2.namedWindow("TOZERO_INV", cv2.WINDOW_NORMAL)

        ret, thr1 = cv2.threshold(self.frame, 127, 255, cv2.THRESH_BINARY)
        ret, thr2 = cv2.threshold(self.frame, 127, 255, cv2.THRESH_BINARY_INV)
        ret, thr3 = cv2.threshold(self.frame, 127, 255, cv2.THRESH_TRUNC)
        ret, thr4 = cv2.threshold(self.frame, 127, 255, cv2.THRESH_TOZERO)
        ret, thr5 = cv2.threshold(self.frame, 127, 255, cv2.THRESH_TOZERO_INV)
        
        # cv2.THRESH_BINARY: threshold보다 크면 value이고 아니면 0으로 바꾸어 줍니다. 
        # cv2.THRESH_BINARY_INV: threshold보다 크면 0이고 아니면 value로 바꾸어 줍니다.   
        # cv2.THRESH_TRUNC: threshold보다 크면 value로 지정하고 작으면 기존의 값 그대로 사용한다. 
        # cv2.THRESH_TOZERO: treshold_value보다 크면 픽셀 값 그대로 작으면 0으로 할당한다. 
        # cv2.THRESH_TOZERO_INV: threshold_value보다 크면 0으로 작으면 그대로 할당해준다. 


        cv2.imshow("BINARY", thr1)
        cv2.imshow("BINARY_INV", thr2)
        cv2.imshow("TRUNC", thr3)
        cv2.imshow("TOZERO", thr4)
        cv2.imshow("TOZERO_INV", thr5)



    def close_windows(self):
        cv2.destroyAllWindows('frame')


def main():
    editor = MyWindow()
    editor.show_camera()

if __name__ == "__main__":
    main()