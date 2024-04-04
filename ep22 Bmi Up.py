#BMI
weight = int(input("ป้อนน้ำหนัก (kg) :"))
high = int(input("ป้อนส่วนสูง (cm) :"))/100
bmi = weight/(high**2)

print("BMI =",bmi)

result = "ไม่ทราบค่าที่ชัดเจน"
if bmi < 18.0 and bmi >= 0:
    result = "ต่ำกว่าเกณฑ์"
elif bmi >= 18.5 and bmi <= 22.9:
    result = "สมส่วน"
elif bmi >= 23.0 and bmi <= 24.9:
    result = "น้ำหนักเกิน"
elif bmi >= 25.0 and bmi <= 29.9:
    result = "โรคอ้วนระดับ 1"
elif bmi > 30:
    result = "โรคอ้วนอัตราย"
else:
    result = "ไม่ทราบค่าที่ชัดเจน"

print(result)