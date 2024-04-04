#แม่สูตรคูณ

start = int(input("สูตรคูรแม่ :"))
stop = int(input("ถึงแม่ :"))
for x in range(start,stop+1):
    print("สูตรคูรแม่ :",x)
    for y in range(0,12+1):
        print(x,"x",y,"=",x*y)