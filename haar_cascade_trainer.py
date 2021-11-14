import numpy as np
import cv2
import aux_methods
import imutils
import os
"""
Script de reconocimiento de imagen e identificación acorde con el entrenamiento del HaarCascade
"""
data_pos = 'data_haarcascade/p'
data_neg = 'data_haarcascade/n'

if not os.path.exists(data_pos):
    print('Carpeta creada: ', data_pos)
    os.makedirs(data_pos)
if not os.path.exists(data_neg):
    print('Carpeta creada: ', data_neg)
    os.makedirs(data_neg)


cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
x1, y1 = 175, 70
x2, y2 = 425, 320

count = 0
count_neg = 0


while True:
    ret, frame = cap.read()
    if ret == False:
        break
    
    im_aux = frame.copy()
    cv2.rectangle(frame,(x1,y1),(x2,y2), (255,102,34), 2)
    cap_face = im_aux[y1:y2, x1:x2]
    cap_face = imutils.resize(cap_face, width=24)
    k = cv2.waitKey(1) #Se declara una variable con el resultado de llamar a WaitKey porque mejora sustancialmente el tiempo de ejecución, si no, no se puede ejecutar el if del guardado tan rápido como quiera el usuario hacer click
    if k == ord('q'):
        break
    if k == ord('s'):
        cv2.imwrite(data_pos+'/objeto_{}.jpg'.format(count),cap_face)
        print('Saved image: ','objeto_{}.jpg'.format(count))
        count= count +1
    if k == ord('n'):
        cv2.imwrite(data_neg+'/objeto_neg_{}.jpg'.format(count_neg),cap_face)
        print('Saved image: ','objeto_neg_{}.jpg'.format(count_neg))
        count_neg = count_neg +1
    
    cv2.imshow('frame general', frame)
    cv2.imshow('frame para datos',cap_face)
    
cap.release()
cv2.destroyAllWindows()

if __name__ == "__main__":
    pass