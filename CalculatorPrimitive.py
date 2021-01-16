i=int(input())


def primitiveCalculator(x):

    l=[x]
    if x<3:
        if x==1:
            return [1]
        if x==2:
            return [1,2]
    else:
        while (x!=1) :

            r3=x%3
            r2=x%2
            if (r3 == 0) and (r2 == 0):
                x = int(x / 3)
                l.append(x)

            if r3==0:
                x = int(x / 3)
                l.append(x)
            if r2==0:
                x = int(x / 2)
                l.append(x)
            if (r3!=0) and (r2!=0):
                if r3<r2:
                    for t in range(0, r3):
                        x = x - 1
                        l.append(x)
                    x = int(x / 3)
                    l.append(x)
                else:
                    for t in range(0, r2):
                        x = x - 1
                        l.append(x)
                    x = int(x / 2)
                    l.append(x)
        return l

op=primitiveCalculator(i)
op.reverse()
print(len(op)-1)
for j in op:
    print(j,end=" ")
