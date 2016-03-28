t=input()
for _ in xrange(t):
    num = raw_input()
    count = 0
    for char in num:
        number = int(num)
        digit = int(char)
        if digit != 0 and number%digit == 0:
            count += 1
    print count
