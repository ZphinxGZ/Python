#Loop
'''
while expression :
    statement
'''

# i=1
# while i<=10 :
#     print("รอบที่ :",i)
#     print("เริ่ม loop ใหม่ครั้งที่",i)
#     i = i+1
    
# print("จบโปรแกรม")

# i = 1
# summation = 0
# count = int(input("ระบุจำนวนรอบ :"))

# while i<=count:
#     summation += i
#     print("รอบที่ :",i,"ค่า sum",summation)
#     i += 1

# average = summation/count
# print("ผลรวม",summation)
# print("ค่าเฉลี่ย =",average)

'''
รู้จำนวนรอบที่ชัดเจน
for in range() #กำหนดรอบ start stop step
'''

# for i in range(6): #(start,stop(มองเป้น-1),step)
#     print("รอบที่ :",i+1,"HelloWorld")
# summation = 0
# for i in range(1,11):
#     print("รอบที่ :",i,"sum = ",summation)
#     summation = summation+i
# print("ผลรวม :",summation)
# print("ค่าเฉลี่ย :",summation/10)

for i in range(10,0,-1):
    print("รอบที่ :",i)