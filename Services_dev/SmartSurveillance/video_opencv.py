import cv2
from video_base import VideoBase


'''
Video class to process video stream from live camera or video file
'''
class Video(VideoBase):
    
    # video_source: either camera id or video file
    @staticmethod
    def frames():
        videostream = cv2.VideoCapture(VideoBase.video_source)
        if not videostream.isOpened():
            raise RuntimeError('Could not start videostream.')

        while True:
            # read current frame
            ret, img = videostream.read()

            #verify frame
            if(not ret):
                print("No frame from video stream!")
                break
            
            # encode as a jpeg image and return it
            yield cv2.imencode('.jpg', img)[1].tobytes()
        videostream.release()

