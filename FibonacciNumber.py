l=[23,3719]
i=int(input())




for j in range (i-1):
    l.append(l[-1]+l[-2])
    if len(l) > 2:
        l = [l[-2], l[-1]]
if i==0:
    print("0")
elif i==1:
        print('1')
else:
    #print(l[-1])
    a=l[-1]
print(a)



