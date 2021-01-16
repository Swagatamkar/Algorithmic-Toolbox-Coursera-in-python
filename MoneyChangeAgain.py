x=int(input())
coins=[1,3,4]
Money=list()
for t in range(1,x+1):
    Money.append(t)

def MoneyChangeAgain(m,c):
    a=[0]
    for z in m:
        Minnumofcoins=99999999999999999999999999

        for q in c:
            if z>=q:
                NumOfCoins=a[z-q]+1
                if NumOfCoins<Minnumofcoins:
                    Minnumofcoins=NumOfCoins
        a.append(Minnumofcoins)

    return  Minnumofcoins
y=MoneyChangeAgain(Money,coins)
print(y)