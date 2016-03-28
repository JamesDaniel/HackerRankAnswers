from math import sqrt, ceil
t=input()
for _ in range(t):
    a,b = map(int,raw_input().split())
    count = 0
    if a==0:count+=1;a=2
    
    first_square = ceil(sqrt(a))
    while first_square**2 <= b:
        count += 1
        first_square += 1
    print count
