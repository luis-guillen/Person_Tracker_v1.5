import cv2
import numpy as np

# Cargar el clasificador Haar para cuerpo completo
fullbody_cascade = cv2.CascadeClassifier('haarcascade_fullbody.xml')

# Inicializar variables para el seguimiento
tracked_persons = []

cap = cv2.VideoCapture("people_walking.mp4")

# Número de fotogramas consecutivos sin detección antes de considerar que una persona ha abandonado la escena
frames_to_disappear = 15

def is_person_tracked(x, y, w, h):
    for person in tracked_persons:
        prev_x, prev_y, prev_w, prev_h, _ = person['properties']
        if abs(x + w//2 - (prev_x + prev_w//2)) < 30 and abs(y + h//2 - (prev_y + prev_h//2)) < 30:
            return person
    return None

def assign_color():
    return (np.random.randint(0, 256), np.random.randint(0, 256), np.random.randint(0, 256))

while cap.isOpened():
    retVal, frame = cap.read()
    if not retVal:
        break
    frame = cv2.resize(frame, (800, 600))  # Aumentar tamaño para una mejor detección

    # Convertir a escala de grises para el clasificador Haar
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detección inicial usando Haar Cascade con ajustes de parámetros
    bodies = fullbody_cascade.detectMultiScale(
        gray_frame,
        scaleFactor=1.05,
        minNeighbors=8,
        minSize=(30, 30),  # Ajustar el tamaño mínimo para la detección
    )

    # Actualizar la lista de personas rastreadas
    for (x, y, w, h) in bodies:
        tracked_person = is_person_tracked(x, y, w, h)
        if tracked_person:
            tracked_person['properties'] = (x, y, w, h, tracked_person['properties'][4])  # Mantener el color existente
            tracked_person['frames_without_detection'] = 0
        else:
            color = assign_color()
            person_id = len(tracked_persons) + 1
            while any(person['id'] == person_id for person in tracked_persons):
                person_id += 1
            tracked_persons.append({'id': person_id, 'properties': (x, y, w, h, color), 'frames_without_detection': 0})

    # Dibujar rectángulo y etiqueta para cada persona
    for person in tracked_persons:
        x, y, w, h, color = person['properties']
        cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
        cv2.putText(frame, f'Persona {person["id"]}', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

    # Verificación de seguimiento y eliminación de personas ausentes
    for person in tracked_persons:
        person['frames_without_detection'] += 1

    tracked_persons = [person for person in tracked_persons if person['frames_without_detection'] < frames_to_disappear]

    cv2.imshow('frame', frame)
    if cv2.waitKey(5) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
