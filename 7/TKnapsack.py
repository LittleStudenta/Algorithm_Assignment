
def __main():
    weight = [4, 2, 5,]
    bulk = [1, 2, 3,]
    value = [5, 2, 6,]
    cw = 5
    cb = 4
    n = len(weight)
    m = [ [[0,0] for j in range(max(cw,cb))] 
            for i in range(n) 
        ]
    print(m)
    tk(weight,bulk,value,m, n,cw,cb)
 

def tk(w,b,v,m, n,cw,cb,):
    for i in range(n-1,-1,-1):
        maxew = min(w[i], cw)
        maxeb = min(b[i], cb)
        maxe = max(maxew, maxeb)

        if i == n:
            for j in range( maxe ):
                m[i][j] =[0, 0]
            #for j in range(maxe, max(cb, cw)+1):

            j = maxe
            while j <= max(cb, cw):    
                m[i][j] = [v[i],v[i]]
                j += 1
        else:  
            for j in range( maxe ):
                m[i][j] =m[i+1][j]
            for j in range(maxe, max(cb, cw)+1):
                if j>b[i]+1:
                    m[i][j][0] = max(m[i+1][j][0], m[i+1][j-w[i]][0]+v[i] )
                    m[i][j][1] = max(m[i+1][j][1], m[i+1][j-b[i]][1]+v[i] )
                        
                    m[i][j][0] = min(m[i][j][0], m[i][j][1])
                    m[i][j][1] = m[i][j][0]





__main()
