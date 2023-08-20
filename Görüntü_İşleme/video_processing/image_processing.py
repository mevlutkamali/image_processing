
import cv2
import time

video = cv2.VideoCapture('skynet_machine.mp4')

print("Width :", video.get(3))
print("Height :", video.get(4))

if video.isOpened() == False:
    print("Erorr !..")
    """
        .isOpened() : Bir video veya kamera akışı açtığınızda, bu akışın başarıyla açılıp açılmadığını doğrulamak için .isOpened() yöntemini kullanabilirsiniz. Eğer akış başarıyla açıldıysa, .isOpened() yöntemi True değerini döndürecektir. Aksi takdirde, False değerini döndürecektir .
    """


while True:
    ret, frame = video.read()

    if ret == True:
        time.sleep(0.04)
        cv2.imshow('Video', frame)q
    else:
        break

    if cv2.waitKey(1) == ord("q"):
        break

video.release()
cv2.destroyAllWindows()
