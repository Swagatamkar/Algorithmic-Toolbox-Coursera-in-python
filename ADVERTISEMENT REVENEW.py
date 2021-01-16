i=int(input())
x=input().split()
c=input().split()
money=list()
clicks=list()
for yy in x:
    money.append(int(yy))
for tt in c:
    clicks.append(int(tt))
price=sorted(money,reverse=True)
clc=sorted(clicks,reverse=True)
sum=0
for y in range (0,i):
    sum=sum+(price[y]*clc[y])
print(sum)


