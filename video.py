import cv2

face_cascades = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# img = cv2.imread('face2.jpg')
# img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# faces = face_cascades.detectMultiScale(img_gray)

# for (x, y, w, h) in faces:
#     # x,y -начальные координаты найденого лица(рамки), w и h - высота и ширина рамки, 0,0,255-цвет, 3-толщина рамки
#     cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 3)

# cv2.imshow('result', img)
# cv2.waitKey(0)


cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

while True:
    success, frame = cap.read()
    
    img_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascades.detectMultiScale(img_gray)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 3)

    cv2.imshow('result', frame)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break
