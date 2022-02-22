import cv2
import os
import argparse
"""
Script de reconocimiento de imagen e identificación acorde con el entrenamiento del HaarCascade
"""

def run(name):
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    x1, y1 = 175, 70
    x2, y2 = 425, 320

    count = 0
    count_neg = 0


    while True:
        ret, frame = cap.read()
        if ret == False:
            break
        custom_cascade = cv2.CascadeClassifier('data_haarcascade/classifier/cascade.xml')
        gray_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #Hacemos esto porque el clasificador necesita imagenes en blanco y negro
        faces = custom_cascade.detectMultiScale(gray_image, 9, 150, minSize=(70,78)) #1.3 es el scaling de la imagen con respecto a las imagenes con las que se entrenó el modelo, 5 es el minNeighbours (afecta a la calidad y al numero de detecciones)


        for(x,y,w,h) in faces: #detectMultiScale devuelve un rectángulo. x,y son las coordenadas de la esquina superior izquierda, (x+w),(y+h) hacen la esquina inferior derecha pq en open cv el eje y va en positivo hacia abajo
            cv2.rectangle(frame,(x,y),(x+w,y+h), (255,102,34), 4) # el parámetro 4 representa el grosor de la línea del rectángulo
            cv2.putText(frame, name, (x,y-10),3,0.8,(0,255,100),2,cv2.LINE_AA)
            
        cv2.imshow('frame', frame)
        k = cv2.waitKey(1) #Se declara una variable con el resultado de llamar a WaitKey porque mejora sustancialmente el tiempo de ejecución, si no, no se puede ejecutar el if del guardado tan rápido como quiera el usuario hacer click
        if k == ord('q'):
            break
        
        
    cap.release()
    cv2.destroyAllWindows()

def parse_opt():
    parser = argparse.ArgumentParser()
    parser.add_argument('--name', type=str)
    opt = parser.parse_args()
    return opt

def main(opt):
    run(**vars(opt))

if __name__ == "__main__":
    opt = parse_opt()
    main(opt)