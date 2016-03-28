for _ in range(input()):
    money,cost,special = map(int,raw_input().split())
    chocks=money/cost
    wrappers=chocks
    
    while wrappers >= special:
        extras = wrappers/special
        chocks += extras
        wrappers+=extras
        wrappers-= special*extras
    #print 'wrappers: ' + str(wrappers)
    
    print chocks
