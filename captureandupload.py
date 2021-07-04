import cv2
import dropbox
import random
import time

start_time=time.time()
def take_snapshot():
        number=random.randint(0,100)
        print(number)

        videoCaptureObject=cv2.VideoCapture(0)
        result=True
        while(result):
            ret,frame=videoCaptureObject.read()
            img_name="img"+ str(number)+".png"
            cv2.imwrite(img_name,frame)
            result=False
        
        videoCaptureObject.release()
        cv2.destroyAllWindows()
        print("snapshot taken")
        return img_name

def upload_file(img_name):
    access_token="zngRJaAJ704AAAAAAAAAARNNXBTqV8uxN9-sMMsvZuppGJHl4aEXB0g-hZ_tTKsV"
    file=img_name
    file_from=file
    file_to="/security system/"+(img_name)
    dbx=dropbox.Dropbox(access_token)

    with open(file_from,"rb")as f:
        dbx.files_upload(f.read(),file_to,mode=dropbox.files.WriteMode.overwrite)

        print("file uploaded")

def main():
    while(True):
        if((time.time()-start_time)>=40):
            name=take_snapshot()
            upload_file(name)

main()