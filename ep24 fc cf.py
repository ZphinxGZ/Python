# c = float(input("ป้อนอุณหภูมิ Celsius :"))
# cf = (c*9/5)+32
# print("จะได้ :",cf,"Fahrenheit")

# f = float(input("ป้อนอุณหภูมิ Fahrenheit :"))
# fc = (f-32)*5/9
# print("จะได้ :",fc,"Celsius")

temp = input("ป้อนอุณหภูมิ (องศา)") #45c

degree = float(temp[:-1]) #45
unit = temp[-1].upper() #c

#print(degree,unit)
if unit == "C":
    result = (degree*9/5)+32
    print("จะได้ :",result,"Fahrenheit")
if unit == "F":
    result = (degree-32)*5/9
    print("จะได้ :",result,"Celsius")

print("แปลงเลข",degree,"จากหน่วย",unit,"เป็น",result)




