import numpy as np
import cv2
import time
from switch import TestThreading

from watch import Watcher,TimeLimit
from camera_thread import VideoStreamWidget
from just import predict


w = Watcher(0)
t = TimeLimit()

if __name__ == "__main__":
    src = 'rtsp://admin:xx2317xx2317@192.168.5.35' #175.101.82.215:1024/Streaming/Channels/502

    video_stream_widget = VideoStreamWidget(src)
    time.sleep(1)

    while True:

        count = predict(video_stream_widget.frame)

        if count is None:
            time.sleep(10)
            continue

        watch = w.variable < count
        print(watch,w.variable,count)

        if count >= 1 and watch and t.check_value() > 40:
                TestThreading('fea81223099547a195f24ebc5be772a6')
                print('request sent')
                t = TimeLimit(int(time.time()))

        w.check_value(count)
        video_stream_widget.show_frame()
        key = cv2.waitKey(1)
        if key & 0xFF == ord('q'):
            break
