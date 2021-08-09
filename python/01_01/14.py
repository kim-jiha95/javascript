y1 = int(input())

if ((y1 % 4 == 0) and (y1 % 100 !=0 or y1%400==0)):
    print("1")
else: 
    print("0")