import cv2
import spreadSheet as sp
def generate_dataset(img, id, img_id):
    cv2.imwrite("dataset/user." + str(id) + "." + str(img_id) + ".jpg", img)

def draw_boundary(img, classifier, scaleFactor, minNeighbours, color,text, clf):
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    features = classifier.detectMultiScale(gray_img, scaleFactor, minNeighbours)
    coords = []

    for(x, y, w, h) in features:
        cv2.rectangle(img, (x,y), (x+w, y+h), color, 2)
        id, _= clf.predict(gray_img[y:y+h, x:x+w])
        
        id, confi= clf.predict(gray_img[y:y+h, x:x+w])

        print("userid = ", id, " confidence = " ,confi, end ="\n\n")       
        if(confi < 60):
            if (id == 1):
              name = "Aastha"
            elif (id == 2):
              name = "Abhay"
            elif (id == 3):
              name = "Aima"
            elif (id == 4):
              name = "Alamdar Abbas"
            elif (id == 5):
              name = "Aman"
            elif (id == 6):
              name = "Arjun"
            elif (id == 7):
              name = "Ashar"
            elif (id == 8):   
              name = "Ashutosh Dwivedi"
            elif (id == 9):
              name = "Ashutosh Kumar"
            elif (id == 10):
              name = "Dipanshu"
            elif (id == 11):
              name = "Himunshu"
            elif (id == 12):
              name = "Ifra"
            elif (id == 13):
              name = "Isha"
            elif (id == 14):     
              name = "Ishraq"
            elif (id == 15):
              name = "Israil"
            elif (id == 16):
              name = "Kavya"
            elif (id == 17):
              name = "Kunal"
            elif (id == 18):
              name = "Mariam Jamal"
            elif (id == 19):
              name = "Mariam Khan"
            elif (id == 20):     
              name = "Asad"
            elif (id == 21):
              name = "Najir"
            elif (id == 22):
              name = "Atif"
            elif (id == 23):
              name = "Muzzakir"
            elif (id == 24):
              name = "Sahil"
            elif (id == 25):
              name = "Sharique"
            elif (id == 26):
              name = "Shoaib"
            elif (id == 27):
              name = "Touheed"
            elif (id == 28):
              name = "Zahid"
            elif (id == 29):
              name = "Zargham"
            elif (id == 30):
              name = "Moin"
            elif (id == 31):
              name = "Naman"
            elif (id == 32):
              name = "Nausheen"
            elif (id == 33):
              name = "Naval"
            elif (id == 34):
              name = "Nazreen"
            elif (id == 35):
              name = "Nikhil"
            elif (id == 36):
              name = "Pushpendra"
            elif (id == 37):
              name = "Rishi"
            elif (id == 38):
              name = "Shabhat"
            elif (id == 39):   
              name = "Saba"
            elif (id == 40):
              name = "Sandeep"
            elif (id == 41):
              name = "Shaba"
            elif (id == 42):
              name = "Fahad"
            elif (id == 43):
              name = "Shaqib"
            elif (id == 44):
              name = "Shivam"
            elif (id == 45):     
              name = "Shubam"
            elif (id == 46):
              name = "Shubangi"
            elif (id == 47):
              name = "Sumit"
            elif (id == 48):
              name = "Hamid"
            elif (id == 49):
              name = "Tairah"
            elif (id == 50):
              name = "Tarun"
            elif (id == 51):     
              name = "Vaishali"
            elif (id == 52):
              name = "Vinay"
            elif (id == 53):
              name = "Wasif"
            elif (id == 54):
              name = "Wasit"
            elif (id == 55):
              name = "Yogesh"
            elif (id == 56):
              name = "Ives"
            elif (id == 57):
              name = "Zain"
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(img, name, (x,y-4), font, 0.8, color, 1, cv2.LINE_AA)        
            sp.markAttendence(id)
        else:
           font = cv2.FONT_HERSHEY_SIMPLEX
           cv2.putText(img, "Face not recognized....!", (x,y-4), font, 0.8, color, 1, cv2.LINE_AA)

        coords = [x, y, w, h]
    return coords
def recognize(img, clf, faceCascade):
    color = {"blue":(255,0,0),"red": (0,0,255)}

    coords = draw_boundary(img, faceCascade, 1.1, 10, color['blue'], "face", clf)
    return img

def detect(img, faceCascade, img_id):
    color = {"blue":(255, 0, 0), "red":(255, 255, 0)}
    coords = draw_boundary(img, faceCascade, 1.1, 10, color['red'], "face", clf)
    if len(coords) == 4:
        roi_img = img[coords[1] : coords[1]+coords[3],coords[0] : coords[0]+coords[2]]
        user_id = 3 # change the user for each different users
        generate_dataset(roi_img, user_id, img_id)

    return img

faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
clf = cv2.face.LBPHFaceRecognizer_create()
clf.read("classifier.yml")
video_capture = cv2.VideoCapture(0)
img_id  = 0
while True:
    _, img = video_capture.read()
     
    #img = detect(img, faceCascade, img_id)
    img = recognize(img, clf, faceCascade)
    cv2.imshow("face Detection", img)
    img_id = img_id + 1
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
video_capture.release()
cv2.destroyAllWindows()
  
