#เจาะลึก string
name = "kuankorn เกรด 4 อยู่ชั้นปี 4"


# print("มีอายุ",name[-2:]) #ก่อนถึงตำแหน่งสุดท้าย
# print(len(name)) #len()เอาไว้หาความยาวของ String


# print(len(name))
# name = name.strip() #.strip() .lstrip() .rstrip() เอาไว้ลบช่องว่างซ้ายขวา
# print(len(name))

#แปลง string เป็นพิมใหญ่
#ใช้ .upper()
#ใช้ .lower()
#ใช้ .capitalize()
#ใช้ .replace("ข้อความ")

# print(name.upper()) #ตัวใหญ่
# print(name.lower()) #ตัวเล็ก
# print(name.capitalize()) #ตัวหน้าใหญ่
# print(name.replace("4","5")) #เปลี่ยนข้อความ
# print(name.replace("4","5",1)) #เปลี่ยนข้อความตัวเดียวโดยใส่ตัว count

# name1 = "ไปซื้อข้าวและอาหารที่ตลาด"
# x = "ข้าว" in name1
# print(x)
# if x:
#     name1 = name1.replace("ข้าว","ไข่")
# print(name1)


#concatinate +
# fname = "Kunakorn"
# lname = "Khamcharoen"
# age = "21"
# job = "Programer"

# fullname = fname+lname+age
# print("ชื่อจริง :",fname,"นามสกุล :",lname,"อายุ :",age)

# text = "ชื่อจริง :{0}\tนามสกุล :{1}\tอายุ :{2}\tอาชีพ :{3}\tเงินเดือน :{4:.2f}"
# print(text.format(fname,lname,age,job,500))

#นับจำนวนประโยค
# fruit = "ไปซื้อผลไม้ มีทุเรียน มังคุด ข้าวเหนียวทุเรียน ที่ตลาด จะแวะไปสวนทุเรียนด้วย"

# print(fruit.count("ทุเรียน")) #นับจำนวนคำในประโยค

# name = "นายกอไก่ ใจดี"
# #.startswith() เข้คคำขึ้นต้น
# # print(name.startswith("นาย"))
# if name.startswith("นาย"):
#     print("เพศชาย")
# else:
#     print("เป็นบุคคลอื่น")


name = "1150"

#.endswitch() เช้คคำลงท้าย
if name.endswith("0"):
    print("ถูกหวย")
else:
    print("ไม่ถูกหวย")












