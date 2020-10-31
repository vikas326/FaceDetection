import face_fetch
import os
import cv2
dir_path = "vikas"
target_path = "faces"

# face_fetch.fetch("abc.jpg")
def main():
    print(os.listdir(dir_path))
    filelist = os.listdir(dir_path)
    i=0
    for file_name in filelist:
        print(file_name)
        faces = face_fetch.fetch(dir_path+'/'+file_name)
        # print('faces fetch')
        # print(faces)
        for face in faces:
            cv2.imwrite(target_path+'/face'+str(i)+'.jpg', face)
            i = i+1
if __name__=="__main__":
    main()