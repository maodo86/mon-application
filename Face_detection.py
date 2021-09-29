import cv2 as cv
 
#Reading video

capture = cv.VideoCapture(0)   #chemin video, 0 pour le webcam, 1: pour une camera branchée
face_cascade=cv.CascadeClassifier(r"C:\Users\dell\Documents\Perso\haar-cascade-files-master\haarcascade_frontalface_default.xml")
profile_cascade=cv.CascadeClassifier(r"C:\Users\dell\Documents\Perso\haar-cascade-files-master\haarcascade_profileface.xml")
cap=cv.VideoCapture(0)
width=int(cap.get(3))
marge=70

while True:
    val_retour, frame=capture.read()  #lecture frame par frame de la video
    tab_face=[]
    tickmark=cv.getTickCount()        #fonction pour mesurer le temps
    gray=cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    face =face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=6)
    for x,y,w,h in face :
        tab_face.append([x, y, x+w, y+h])
    face =profile_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=6)
    for x,y,w,h in face :
        tab_face.append([x, y, x+w, y+h])
    gray2=cv.flip(gray, 1)
    face_rect =profile_cascade.detectMultiScale(gray2, scaleFactor=1.1, minNeighbors=6)
    for x,y,w,h in face_rect :
        tab_face.append([width-x, y,width-(x+w), y+h])
    
    tab_face=sorted(tab_face)
    index=0
    for x,y, x2, y2 in tab_face:
        if not index or (x-tab_face[index-1][0]>marge or  y-tab_face[index-1][1]>marge):
            cv.rectangle(frame, (x,y), (x2, y2), (0,0, 255), thickness=2)
        index=1
    if cv.waitKey(10) & 0xFF==ord('q'):
         break

    fps=cv.getTickFrequency()/(cv.getTickCount()-tickmark)
    cv.putText(frame, "FPS: {:05.2f}".format(fps), (10,30), cv.FONT_HERSHEY_PLAIN, 2, (0,0,255), 2)
    cv.imshow('Video', frame)


capture.release()
cv.destroyAllWindows()           #ferme toutes les fenetres


#Resizing and Rescaling image and video

#live video
def changeRes(width, height):
    capture.set(3, width)
    capture.set(4, height)


def rescaleFrame(frame, scale=0.2):
    width  =  int(frame.shape[1]*scale)
    height =  int(frame.shape[0]*scale)
    dimensions = [width, height]

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


