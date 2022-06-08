from email.mime import image
import cv2

cap = cv2.VideoCapture(0)
face_detector = cv2.CascadeClassifier(cv2.data.haarcascades +
                                      "haarcascade_frontalface_default.xml")

# metodo
method = 'FisherFaces'
if method == 'FisherFaces': emotion_recognizer = cv2.face.FisherFaceRecognizer_create()

emotion_recognizer.read('modelo' + method + '.xml')
imagePaths = ['Disgustado', 'Enojado', 'Feliz', 'Serio', 'Sorprendido', 'Temerozo', 'Triste']


def obtener_frame_camara():
    ok, frame = cap.read()
    if not ok:
        return False, None
    # Codificar la imagen como JPG
    _ = cv2.imencode(".jpg", frame)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    auxFrame = gray.copy()
    faces = face_detector.detectMultiScale(gray, 1.005,5)
    emocion = ""
    for (x, y, w, h) in faces:
        rostro = auxFrame[y:y + h, x:x + w]
        rostro = cv2.resize(rostro, (48, 48), interpolation=cv2.INTER_CUBIC)
        result = emotion_recognizer.predict(rostro)
        cv2.putText(frame, '{}'.format(result), (x, y - 5), 1, 1.3, (255, 255, 0), 1, cv2.LINE_AA)
        emocion = result
        if result[1] < 500:
            cv2.putText(frame, '{}'.format(imagePaths[result[0]]), (x, y - 25), 2, 1.1, (0, 255, 0), 1,
                        cv2.LINE_AA)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            
        else:
            cv2.putText(frame, 'Desconocido', (x, y - 20), 2, 0.8, (0, 0, 255), 1, cv2.LINE_AA)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
    cv2.destroyAllWindows()
    return emocion

cv2.destroyAllWindows()