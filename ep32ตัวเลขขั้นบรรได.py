#ตัวเลขขั้นบรรได

last = int(input("ป้อนตัวเลขสุดท้าย :"))
for row in range(1,last+1):
    for col in range(1,row):
        print(col,end="")
    print(row)
    