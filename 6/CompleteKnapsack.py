
def __main():

    weight = [4, 2, 1, 3, 5,]
    value = [5, 3, 2, 6, 8,]
    c = 8
    n = len(weight) 
    m = [[0]*c for j in range(n)] 
           
    ck(weight, value, m, n-1, c,)
    print(Trackback(m, n-1, weight, value, c-1))

def ck(w, v, m, n, c,): 
    #放置物品为n时
    for j in range(c):
        num = (j+1) // w[n]
        m[n][j] = num *v[n]
    #n-1~0
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
            x.append(i)
            j -=w[i]
    if m[i+1][j] == 0:
        pass
    else:
        x.append(i)    
    return x       

__main()
