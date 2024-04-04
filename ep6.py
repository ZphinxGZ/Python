#type Coversion
x,y,z = 10,3.14,"20"
print(x,y,z)
print(type(x))
print(type(y))
print(type(z))

#บวกเลข
result = x + y
print(type(result))
print(result)

#แปลงข้อมูล
# result2 = x + int(z)
# result2 = str(x) + z
# print(type(result2))
# print(result2)
print(float(z))
print(int(y))
print(float(x))
x = float(x)
print(type(x),x)