
def __main():
    
    bulk = [1, 2, 3, 4, 5,]  #题目信息
    weight = [4, 2, 1, 3, 5,]
    value = [5, 3, 2, 6, 8,]
    cw = 10
    cb = 9
    n = len(weight) 
    m = [ [[0]*cw for j in range(cb)] #三维数组[n][bulk][weight]
            for i in range(n) 
        ]
    tk(weight, bulk, value, m, n-1, cw, cb)
    print(Trackback(m, n, weight, bulk, cw, cb))

def tk(w,b,v,m, n,cw,cb,):
    ##放置物品为第n个时
    maxew = min(w[n]-1, cw)
    maxeb = min(b[n]-1, cb)
    for j in range( maxeb ):
        for k in range( maxew ):
            m[n][j][k] = 0
    for j in range(maxeb, cb):
        for k in range(maxew, cw):   
            m[n][j][k] = v[n]
        #放置物品为n-1~0
    for i in range(n-1,-1,-1):
        maxew = min(w[i]-1, cw)
        maxeb = min(b[i]-1, cb)
        for j in range( cb ):           #刷一下不被更改的数据
            for k in range( cw ):
                m[i][j][k] =m[i+1][j][k]
        
        for j in range(maxeb, cb):
            for k in range(maxew, cw):
                if j - b[i] < 0:           #有一个小bug
                    j_bi = 0
                else:
                    j_bi = j - b[i]    
                if k - w[i] < 0:
                    k_wi = 0
                else:
                    k_wi = k - w[i]
                m[i][j][k] = max(m[i+1][j][k], m[i+1][j_bi][k_wi]+v[i] )

def Trackback(m, n, w, b, cw, cb):
    j = cb -1
    k = cw -1
    x = []
    for i in range(n-1):
        if m[i][j][k] == m[i+1][j][k]:
            continue
        else:
            x.append(i)
            j -=b[i]
            k -=w[i]      
    if m[i+1][j][k] > 0:
        x.append(i) 
    return x        

__main()
