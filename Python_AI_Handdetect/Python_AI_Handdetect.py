import cv2
from cvzone.HandTrackingModule import HandDetector

def HandTracking():
    cap = cv2.VideoCapture(0) #สร้างอ็อบเจ็กต์ที่ชื่อ cap เพื่อเปิดการเชื่อมต่อกับกล้องเว็บแคมของคอมพิวเตอร์ (เลข 0 หมายถึงกล้องหลัก)
    detector = HandDetector() #ร้างอ็อบเจ็กต์ detector จากคลาส HandDetector เพื่อใช้ในการติดตามมือในวิดีโอ.
    while True:
        ret, frame = cap.read() # อ่านเฟรม (เฟรมคือภาพแต่ละเฟรมในวิดีโอ) จากกล้องเว็บแคมและเก็บผลลัพธ์ในตัวแปร ret (บอกว่าการอ่านเฟรมเสร็จสิ้นสำเร็จหรือไม่) และ frame (เฟรมที่อ่านมา).
        if ret:
            hands, img_out = detector.findHands(frame) #เรียกใช้เมธอด findHands จาก detector เพื่อค้นหาและติดตามมือในเฟรมปัจจุบัน ผลลัพธ์จะเก็บไว้ในตัวแปร hands (ข้อมูลเกี่ยวกับมือที่พบ) และ img_out (เฟรมที่มีกรอบสี่เหลี่ยมรอบมือวาดเสร็จแล้ว).
            cv2.imshow('img_out', img_out) # แสดงภาพที่ประมวลผลแล้ว (มีกรอบสี่เหลี่ยมรอบมือ) ในหน้าต่างชื่อ 'img_out'.
        if cv2.waitKey(1) == ord('q'): # รอรับอินพุตจากแป้นพิมพ์ ถ้าผู้ใช้กดปุ่ม 'q' ในแป้นพิมพ์ โปรแกรมจะหยุดลูป.
            break
    cap.release() # ปิดการเชื่อมต่อกับกล้องเว็บแคม เพื่อคืนทรัพยากร.
    cv2.destroyAllwindows() #: ปิดหน้าต่างทั้งหมดที่เปิดขึ้นโดย OpenCV.

HandTracking()