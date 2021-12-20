from PIL import Image
from PIL import ImageDraw
import numpy
import json
import requests


def predict(img):
    np_img = numpy.array(img)
    payload = {"instances": [np_img.tolist()]}


    url = "http://ec2-3-7-57-150.ap-south-1.compute.amazonaws.com:8501/v1/models/img_classification:predict"

    r = requests.post(url,json = payload)

    r1 = json.loads(r.text)

    try:

        r2 = dict(zip(r1['predictions'][0]['detection_scores'],r1['predictions'][0]['detection_classes']))

        r3 = r1['predictions'][0]['detection_boxes']

    except:

        print(r1)

        return None

    # r3 = [i for i in r2 if i > 0.8 and r2[i] == 1.0]

    return r3

if __name__ == '__main__':
    import cv2

    test = cv2.imread('test.jpg')
    img = Image.open('test.jpg')
    res = predict(test)
    print(res)
    draw = ImageDraw.Draw(img)
    im_width, im_height = img.size
    print(im_width, im_height)

    for (x,y,w,h) in res:
        (left, right, top, bottom) = (y * im_width, h * im_width, x * im_height, w * im_height)
        a,b,c,d = map(int,(left, right, top, bottom))
        cv2.rectangle(test, (b,a),(d,c),(0,255,0),2)

    
    font = cv2.FONT_HERSHEY_SIMPLEX

    org = (50, 50)

    fontScale = 1

    color = (255, 0, 0)

    thickness = 2

    image = cv2.putText(test, 'OpenCV', org, font, fontScale, color, thickness, cv2.LINE_AA)

    cv2.imshow('Image',test)


    cv2.waitKey(0)
    cv2.destroyAllWindows()