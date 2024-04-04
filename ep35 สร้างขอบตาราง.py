#สร้างขอบตาราง

number = int(input("ป้อนตัวเลขที่จะสร้าง :"))

for row in range(number):
    for col in range(number):
        if row == 0 or row == number-1 or col == 0 or col == number-1:
            print("x",end="")
        else:
            print(" ",end="")
        
    print("")