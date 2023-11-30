import cv2
flags = [i for i in dir(cv2) if i.startswith('COLOR_')]

if __name__ =="__main__":
    for flag in flags:
        print(flag)