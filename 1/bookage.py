#最初的办法，有大bug，超出200会有误差
def __main():
    count = [0]*10
    num = 12345 
    
    shit(num,count,1)
    count[0]-=11  #这一行纠正了shit递归0多的问题 
    print(count)
    
def shit(n,count,m=10):  
                         #multi是指拆出一个十位为基的小倍数， 
	                     #新数组中的数都需乘以此数，数目方能对应  
    if n==-1:
        return 0
    multi=m
    counta = [0]*10
    ones = n%10
    tens = n//10-1           #这里减一也很好理解，体会一下 
    s = n//10
    t=s
    i=0
    # 例317 先加310~317的各位
    for i in range(0,ones+1):
        counta[i]+=1
        while t:
            counta[t%10]+=1
            t//=10
        t = s
    #再加0~310中的个位
    for i in range(0,10):
        counta[i]+=s
    for i in range(0,10):
        count[i]=count[i]+counta[i]*multi
    #再计算31中的各个位，出来乘以相应倍数
    shit(tens,count)
    return 0
__main()

