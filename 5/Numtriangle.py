
def __main():
    #干嘛要压抑自己，写到main里多舒服a
    b = open('F:\\_Algorithm_Assignment\\5\\input.txt')
    n = int(next(b))
    
    a = [0]*n
    
    for i in range(n) :
        c = next(b)[0:-1]
        a[i] = [int(i) for i in c.split(' ')] 
   
    f = shit(a, n-1)
    print(f)



def shit(tree, h):
    for i in range(h):
        tree[h-1][i] = max(tree[h][i], tree[h][i+1]) + tree[h-1][i]
    if h > 0:
        shit(tree, h-1)

    return tree[0][0]



__main()    
