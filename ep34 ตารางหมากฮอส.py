#ตารางหมากฮอส

number = int(input("ป้อนตัวเลขที่จะสร้าง :"))

for row in range(number):
    for col in range(number):
        if (row+col)%2 == 0:
            print("x",end="")
        else:
            print("o",end="")
    print("")