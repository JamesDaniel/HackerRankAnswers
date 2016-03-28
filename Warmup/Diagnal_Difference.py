
n = int(raw_input())
j = n-1
a = 0
b = 0

for i in xrange(n):
    arr = map(int,raw_input().split())
    a += arr[i]
    b += arr[j]
    j -= 1

print abs(a - b)
   
