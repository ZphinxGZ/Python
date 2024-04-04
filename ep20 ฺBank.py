#แลกเงินและหาจำนวนแบงค์

number = int(input("จะแลกเงินกี่บาท :"))

if number >= 1000:
    print("แบงค์ 1000 บาท =",number//1000,"บาท")
    number %= 1000
if number >= 500:
    print("แบงค์ 500 บาท =",number//500,"บาท")
    number %= 500
if number >= 100:
    print("แบงค์ 100 บาท =",number//100,"บาท")
    number %= 100
if number >= 50:
    print("แบงค์ 50 บาท =",number//50,"บาท")
    number %= 50
if number >= 20:
    print("แบงค์ 20 บาท =",number//20,"บาท")
    number %= 20

print("เหลือเศษ =",number,"บาท")