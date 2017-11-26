
def __main():

    weight = [4, 2, 3, 4, 5,]
    value = [5, 1, 6, 8, 6,]
    c = 10
    n = len(weight) 
    m = [[0]*c for j in range(n)] 
           
    ck(weight, value, m, n-1, c,)
    print(Trackback(m, n-1, weight, value, c-1))

def ck(w, v, m, n, c,): 
    #放置物品为第n个时
    for j in range(c):
        num = (j+1) // w[n]
        m[n][j] = num *v[n]
    #放置物品为n-1~0
    for i in range(n-1,-1,-1):
        for j in range(c):
            num = (j+1) // w[i]
            if j - num*w[i] < 0:
                j_num_wi = 0
            else:
                j_num_wi = j-num*w[i]    
            m[i][j] = max(m[i+1][j], m[i+1][j_num_wi]+num*v[i])          

def Trackback(m, n, w, v, c):
    j = c
    x = []
    for i in range(n):
        if m[i][j] == m[i+1][j]:
            continue
        else:
            count = 0
            k = j
            x.append(i)
            while m[i][k]-m[i][k-1] == 0 or m[i][k]-m[i][k-1] == v[i] and k >0:
                count +=1
                k -= 1 

            x.append(count)
            x.append("   ")    
            j -=w[i]
    if m[i+1][j] == 0:
        pass
    else:
        x.append(i)    
    return x       

__main()
