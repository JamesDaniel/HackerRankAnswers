n = int(input())
neg = 0
neu = 0
pos = 0

arr = map(int, input().split())

for num in arr:
    if (num<0):
        neg += 1
    elif (num>0):
        pos += 1
    else:
        neu += 1
print (pos/n)
print (neg/n)
print (neu/n)
