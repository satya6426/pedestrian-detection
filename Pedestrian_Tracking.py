import cv2

video = cv2.VideoCapture('Pedestrian.mp4')

pedestrian_tracker_file = 'Pedestrians_detector.xml'

pedestrian_tracker = cv2.CascadeClassifier(pedestrian_tracker_file)

while True:

    (read_successful, frame) = video.read()

    if read_successful:

        grayscaled_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    else:

        break

    pedestrians = pedestrian_tracker.detectMultiScale(grayscaled_frame)

    for (x, y, w, h) in pedestrians:
        
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
                    #top left point #bottom right point # Bgr #rec thickness
    cv2.imshow('Pedestrian', frame)

    key = cv2.waitKey(1)

    if key == 81 or key == 113:

        break

video.release()




