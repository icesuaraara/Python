import csv
import os

filename = 'bills.csv'
bath_per_unit = 7 

# อ่านข้อมูลจากไฟล์
def read_last_two_entries(filename):
    entries = []
    with open(filename, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            entries.append(row)
    if len(entries) < 2:
        # ถ้ามีแต่ละคอลัมมีค่าน้อยกว่า 2 บรรทัดให้คืน None
        return None, None
    # รับข้อมูลรองล่าสุดมา
    return entries[-2], entries[-1]

# นำค่าไฟเก่ามาลบกับค่าไฟใหม่
def calculate_differences(previous, latest):
    diff_icesu = int(latest['icesu']) - int(previous['icesu'])
    diff_phoom = int(latest['phoom']) - int(previous['phoom'])
    return diff_icesu, diff_phoom

# เช็คว่ามีไฟล์ไหม
file_exists = os.path.isfile(filename)

# Prompt for user input
icesu = int(input('(icesu)ใส่เลขมิเตอร์ปัจจุบัน : '))
phoom = int(input('(phoom)ใส่เลขมิเตอร์ปัจจุบัน : '))
sum_bill = int(input('(sum)หน่วยไฟเดือนนี้ที่เรียกเก็บ : '))

# เปิดไฟล์แล้วเพิ่มข้อมูล
with open(filename, 'a', newline='') as csvfile:
    fieldnames = ['icesu', 'phoom']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    # ถ้าไฟล์ว่างเปล่าให้สร้างคอลัม
    if not file_exists:
        writer.writeheader()

    # เขียนข้อมูลลงไป
    writer.writerow({'icesu': icesu, 'phoom': phoom})

# คำนวนค่าไฟ
if file_exists:
    previous_entry, latest_entry = read_last_two_entries(filename)
    if previous_entry and latest_entry:
        diff_icesu, diff_phoom = calculate_differences(previous_entry, latest_entry)
        total_diff = diff_icesu + diff_phoom
        result = sum_bill - total_diff 
        diff_icesu += result/2
        diff_phoom += result/2
        print('หน่วยไฟเดือนนี้ของ icesu:', diff_icesu)
        print('หน่วยไฟเดือนนี้ของภูมิ:', diff_phoom)
        print('จำนวนเงินที่ต้องจ่ายของ icesu :', diff_icesu*bath_per_unit,' Bath')
        print('จำนวนเงินที่ต้องจ่ายของ phoom :', diff_phoom*bath_per_unit,' Bath')
    else:
        print('ไม่มีข้อมูลให้คำนวน')
else:
    print('รายการแรกจะไม่มีการคำนวน')

print('รายการค่าไฟถูกเขียนแล้ว : ', filename)
