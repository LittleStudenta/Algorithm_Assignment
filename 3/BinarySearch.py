
#二分法查找某数，没有则返回它附近的两个数
def __main():
    n = 8
    x = 6
    c = [0,1,2,4,5,6,7,8,9,]
    print(BinarySearch(c,x,n))

def BinarySearch(a,x,n):
    left = 0
    right = n
    while right >= left:
        m = (left+right)/2
        
        if x == a[m]: 
            return m
        elif x < a[m]: 
            right = m-1   #在前半段
        else: 
            left = m+1
        
        if right == left and a[right] < x :
            return left,left+1
        elif right == left and a[right] > x :
            return left-1,left
__main()
