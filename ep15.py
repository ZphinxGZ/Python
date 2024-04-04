'''
if expression:
    statement
'''
age = int(input("ป้อนอายุของคุณ :"))
name = "คุณากร"

# if(age <= 15):
#     print("เด็กชาย",name)
# else:
#     print("นาย",name)

'''
if จริง :
    ทำอะไร
else :
    ทำอะไร
'''

# if age >= 15 and age <= 20:
#     print("วัยรุ่น")
# elif age >= 21 and age <= 29:
#     print("วัยทำงาน")
# elif age >= 30 and age <= 39 :
#     print("ผู้ใหญ่")
# elif age >= 40:
#     print("เริ่มแก่และไอสัส")
# else :
#     print("วัยเด็ก")
# print("จบโปรแกรม")

#Ternary Operator
print("วัยรุ่น") if age >= 15 else print("วัยเด้ก")

print("จบโปรแกรม")

