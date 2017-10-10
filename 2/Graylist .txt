def __main():
    n = 3
    a = 2**n
    gray =[([0]*(n+1)) for i in range(a)]
    gray_m(n,gray)

    for j in range(a):
        print(gray[j])

def gray_m(n,gray):
    if n == 0:
        return 0
    else:       
        gray_m(n-1,gray)    
    a = 2**n
    a2 = a//2

    for i in range(a2):
        gray[i][n] = 0
    for i in range(a2,a):
        gray[i][n] = 1    
        
        for j in range(n):
            gray[i][j] = gray[a-i-1][j] 
    return 0        

__main()

