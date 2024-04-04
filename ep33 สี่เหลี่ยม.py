#สร้างสี่เหลี่ยม 

number = int(input("ป้อนตัวเลขที่จะสร้าง :"))

for row in range(number):
    for col in range(number):
        print("*",end="")
    print("")