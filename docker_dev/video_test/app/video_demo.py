import sys
import os
import cv2

'''play local video file'''
def video_show(video_file):
    cap = cv2.VideoCapture(video_file)

    while(1):
        ret,frame = cap.read()

        #verify frame
        if(not ret):
            print("No frame from camera!")
            break
        # shown frame on window
        cv2.imshow('Play video test',frame)

        k = cv2.waitKey(33) & 0xff
        if k == 27:
            break

    cap.release()
    cv2.destroyAllWindows()

'''play local camera'''
def camera_show(camera_id):
    camera = cv2.VideoCapture(camera_id)
    if(not camera.isOpened()):
    	raise RuntimeError('Could not start camera.')

    while(1):
        ret,frame = camera.read()

        #verify frame
        if(not ret):
            print("No frame from camera!")
            break
        # shown frame on window
        cv2.imshow('Play camera test',frame)

        k = cv2.waitKey(33) & 0xff
        if k == 27:
            break

    camera.release()
    cv2.destroyAllWindows()


'''
Function: Provide command line interface for user
''' 
if __name__ == "__main__":
	if(len(sys.argv)<2):
		print("Usage: %s --video|camera ")
		exit()
	
	# play local video file    
	if(sys.argv[1]=="--video"):
		video_show("./res/vtest.avi")
	# launch camera
	elif(sys.argv[1]=="--camera"):
		camera_show(0)
	else:
		print("Unknown command: %s" %(sys.argv[1]))
	pass

