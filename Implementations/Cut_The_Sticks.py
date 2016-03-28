n=input()
arr = map(int,raw_input().split())

while len(arr) >0:
    mini = min(arr)
    count=0
    i=0
    while i < len(arr):
        if arr[i] > 0:
            arr[i] = arr[i]-mini
            if arr[i] <=0:arr.remove(arr[i]);i-=1
            count +=1
        i+=1
    print count

