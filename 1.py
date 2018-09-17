import cv2
import pygame
import time
import numpy as np
def openvideo(window_name,window_name1,video_id):
    global flag1
    global flag2
    flag1=0
    flag2=0
    pygame.mixer.pre_init(44100, -16, 12, 512)
    pygame.init()

    C5 = pygame.mixer.Sound('samples/1.wav')
    C5.set_volume(.80)
    D5 = pygame.mixer.Sound('samples/2.wav')
    D5.set_volume(.80)
    E5= pygame.mixer.Sound('samples/3.wav')
    E5.set_volume(.80)
    F5 = pygame.mixer.Sound('samples/4.wav')
    F5.set_volume(.80)
    G5 = pygame.mixer.Sound('samples/5.wav')
    G5.set_volume(.80)
    A5 = pygame.mixer.Sound('samples/6.wav')
    A5.set_volume(.80)
    B5 = pygame.mixer.Sound('samples/7.wav')
    B5.set_volume(.80)
    C6 = pygame.mixer.Sound('samples/1h.wav')
    C6.set_volume(.80)
    
    cv2.namedWindow(window_name)
    cv2.namedWindow(window_name1)
    cap=cv2.VideoCapture(video_id)
    while cap.isOpened():
        ok,frame=cap.read()
        if not ok:
            break

        grayPic=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)#灰度图
        gaussianPic=cv2.GaussianBlur(grayPic,(5,5),0)#高斯滤波
        ret,threshPic=cv2.threshold(gaussianPic,254,255,cv2.THRESH_BINARY)#阈值化

        image,contours,hierarchy=cv2.findContours(threshPic,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        if contours:
            print('get')
            cnt=contours[0]
            M=cv2.moments(cnt)
            if M['m00']!=0:
                cX=int(M['m10']/M['m00'])
                #cY=int(M['m01']/M['m00'])
                print('x:',cX)
                #print('y:',cY)
                if 100<cX<150:
                    flag1=1
                elif 155<cX<210:
                    flag1=2
                elif 210<cX<265:
                    flag1=3
                elif 265<cX<320:
                    flag1=4
                elif 320<cX<375:
                    flag1=5
                elif 375<cX<430:
                    flag1=6
                elif 430<cX<485:
                    flag1=7
                elif 485<cX<540:
                    flag1=8
                
            if flag1!=flag2:
                if flag1==8:
                    C5.play()
                elif flag1==7:
                    D5.play()
                elif flag1==6:
                    E5.play()
                elif flag1==5:
                    F5.play()
                elif flag1==4:
                    G5.play()
                elif flag1==3:
                    A5.play()
                elif flag1==2:
                    B5.play()
                elif flag1==1:
                    C6.play()
                flag2=flag1
                time.sleep(0.1)
            else:
                flag2=0
                #time.sleep(0.05)
        cv2.imshow(window_name1,frame)
        cv2.imshow(window_name,image)
        c=cv2.waitKey(10)
        if c &0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyWindow(window_name)
    cv2.destroyWindow(window_name1)


        
if __name__ =='__main__':
    print('open camera')
    openvideo('openvideo','openvideo1',0)
