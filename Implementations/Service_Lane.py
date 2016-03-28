n,t = map(int,raw_input().split())
width = [int(num) for num in raw_input().split()]
for _ in xrange(t):
    i,j = map(int,raw_input().split())
    print min(width[i:j+1])
