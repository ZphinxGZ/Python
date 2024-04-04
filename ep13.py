weight = int(input("ป้อนน้ำหนักของคุณ (Kg) :"))
high = int(input("ป้อนส่วนสูงของคุณ (Cm) :"))

#process
# high = high/100
high /= 100
bmi = weight/(high*high)

print("BMI ของคุณคือ :",bmi)