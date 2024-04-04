#เกมทายลูกเต๋า

#import ฟังชั่นแรนดอม
import random
#สุ่มเลขลูกเต๋า
myRandom = random.randrange(1,7)
# print(myRandom)
k = 1
print("คุณมีโอกาสตอบ 3 ครั้ง")
print(myRandom)
while True:
    number = int(input("ป้อนตัวเลขของคุณ :"))
    correct = number==myRandom
    #ออกจากโปรแกรม
    if number < 0 or k == 3:
        if correct :
            print("!! ตอบถูกต้อง")
            break
        else:
            print("เสียใจด้วยนะคำตอบคือ :",myRandom)  
        break
     #ใบ้ผู้เล่น
    if not correct:
        if number > myRandom:
            print("น้อยกว่านี้นิดนึง")
        if number < myRandom:
            print("มากกว่านี้นิดนึง")
    
    #ถ้าตอบถูกก่อน       
    if correct :
        print("!! ตอบถูกต้อง")
        break
    # else:
    #     print("เสียใจด้วยย")
        
    
    k += 1

print("จบโปรแกรม")