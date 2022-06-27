import requests
import cv2
import numpy as np
import imutils

# Coloque a sua url. Sempre deixo o 'shot.jpg' no final.
url = "http://localhost:8080/shot.jpg"

# Euquanto recebe dados da url, exiba a janela.
while True:
    img_resp = requests.get(url)
    img_arr = np.array(bytearray(img_resp.content), dtype=np.uint8)
    img = cv2.imdecode(img_arr, -1)
    img = imutils.resize(img, width=800, height=600)
    cv2.imshow('Android_cam', img)

    # Pressione ESC para sair.
    if cv2.waitKey(1) == 27:
        break

cv2.destroyAllWindows()
