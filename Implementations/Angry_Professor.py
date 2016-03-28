t = int(raw_input())

for _ in xrange(t):
    n,k = map(int,raw_input().split())
    a = map(int,raw_input().split())
    present = 0
    for num in a:
        if num<=0:present+=1
    if present<k: print 'YES'
    else: print 'NO'
