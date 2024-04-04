#หาผลรวมยากจำนวนรอบที่กำหนด

start,stop = 1,5
summation,ave= 0,0
while start<=stop:
    number = int(input("ป้อนตัวเลขของคุณ :"))
    summation += number
    
    start += 1
print("ผลรวม =",summation)
print("ค่าเฉลี่ย =",summation/stop)