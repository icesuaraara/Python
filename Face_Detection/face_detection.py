import cv2
# โหลดแม่แบบสำหรับตรวจจับใบหน้า
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# อ่านรูปภาพจากคอมพิวเตอร์
image_path = 'Xie.jpg'  # เปลี่ยนเป็นพาธของรูปที่คุณต้องการใช้
image = cv2.imread(image_path)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# ตรวจจับใบหน้าในรูป
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

# วาดสี่เหลี่ยมรอบใบหน้า
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

# แสดงรูปที่มีการตรวจจับใบหน้าแล้ว
cv2.imshow('Face Detection', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
