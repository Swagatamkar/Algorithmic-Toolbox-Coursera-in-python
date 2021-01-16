d=int(input())
l=int(input())
g=int(input())
v=input().split()
x=[0]
for q in v:
    x.append(int(q))

x.append(d)







def carrefill(x,n,l):
    currentRefill = 0
    NumOfRefill=0
    while currentRefill<=n:
        LastRefill=currentRefill
        while (currentRefill<=n) and (x[currentRefill+1]-x[LastRefill]<=l):
            currentRefill+=1
        if currentRefill==LastRefill:
            print('-1')
            quit()
        if currentRefill<=n:
            NumOfRefill+=1
            #print(NumOfRefill)
    return NumOfRefill
p=carrefill(x,g,l)
print(p)
