#ค้นหาตัวเลขมากสุดน้อยสุด

max,min = 0,9999

while True:
    number = int(input("ป้อนตัวเลขของคุณ :"))
    if number < 0:
        break
    if number > max:
        max = number
    if number < min:
        min = number
        
print("\nค่าสูงสุด =",max)
print("ค่าต่ำสุด =",min)