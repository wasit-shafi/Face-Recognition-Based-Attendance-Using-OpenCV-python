import cv2

def generate_dataset(img, img_id):
    global userId, userName  # using globale variables for userId & userName
    cv2.imwrite("dataset/" + userName + "." + str(userId) + "." + str(img_id) + ".jpg", img)
  
def draw_boundary(img, classifier, scaleFactor, minNeighbours, color,text):
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    features = classifier.detectMultiScale(gray_img, scaleFactor, minNeighbours)
    coords = []

    for(x, y, w, h) in features:
        cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)
        cv2.putText(img, text, (x, y - 4), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 1, cv2.LINE_AA)
        coords = [x, y, w, h]
    return coords

def detect(img, faceCascade, img_id):
    color = {"BLUE":(255, 0, 0), "GREEN":(0,255,0), "RED":(0, 0, 255), "LIMEGREEN":(50, 205, 50)}
    coords = draw_boundary(img, faceCascade, 1.1, 5, color['LIMEGREEN'], "Face Detected...")
    if len(coords) == 4:
        roi_img = img[coords[ 1] : coords[1] + coords[3], coords[0] : coords[0] + coords[2]]
        generate_dataset(roi_img, img_id)
    return img

# Main

faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
videoCapture = cv2.VideoCapture(0)

userId = int(input("Enter user id : "))
userName = input("Enter user name : ")

print("Press 'q' to stop creating dataSet.")
print("Press any key to start...")
input("")

imgId = 1  #data set images of userID  will start form 1...
while True:
    _, img = videoCapture.read()
     
    img = detect(img, faceCascade, imgId)
    cv2.imshow("Data Set Creator", img)
    imgId = imgId + 1
    if cv2.waitKey(20) & 0xff == ord('q'):
        break
videoCapture.release()
cv2.destroyAllWindows()
