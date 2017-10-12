#简单的解决办法
def __main():
    count = [0]*10
    num = 199
    shit(num,count)
    print(count)
    
def shit(n,count):  
    counta = count
    for i in range(0,n+1):
        t = i
        while t:
            counta[t%10]+=1
            t//=10
    count = counta        
    return 0
__main()

