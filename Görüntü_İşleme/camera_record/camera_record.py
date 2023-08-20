
import cv2
import time

camera = cv2.VideoCapture(0)

widths = int(camera.get(cv2.CAP_PROP_FRAME_WIDTH))
heights = int(camera.get(cv2.CAP_PROP_FRAME_HEIGHT))

print(widths, heights)

record = cv2.VideoWriter('record.m4', cv2.VideoWriter_fourcc(*'DIVX'), 24, (widths, heights))

while True:

    ret, frame = camera.read()
    cv2.imshow('record.m4', frame)

    record.write(frame)

    if cv2.waitKey(1) == ord("q"):
        break
