t=input()
for _ in range(t):
    digs = input()
    if digs<3 or digs==4:
        print -1
        continue
    num = '5' * digs
    if num.count('5')%3==0 and len(num)==digs:
        print num
    elif num.count('5')%3!=0:
        num = num[:-5] + '3'*5
        if num.count('5')%3==0 and len(num)==digs:print num
        else:
            num = num[:-10] + '3'*10
            if num.count('5')%3==0 and len(num)==digs:print num
            else: print -1
