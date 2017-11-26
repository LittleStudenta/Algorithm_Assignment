
def __main():
    b = open('F:\\_Algorithm_Assignment\\9\\input.txt')
    n = int(next(b))
    a = [0]*n
    c = next(b)[0:-1]
    a = [int(i) for i in c.split(' ')] 
   
    print(BestServe(a,n))
    c = 1

def BestServe(a,n):
    a = FastSort(a)
    alltime = 0
    for i in range(n):
        alltime += (n-i)*a[i] 
    average = alltime/n
    return average


def FastSort(a):
    length = len(a)
    if length <= 1 :
        return a
    else:
        flag = (length-1)//2
        temp1, temp2, temp3 = [], [], []
        for i in range(length):
            if a[i] < a[flag]:
                temp1.append(a[i])
            elif a[i] == a[flag]:
                temp2.append(a[i])
            else:
                temp3.append(a[i])     

        a = FastSort(temp1) + temp2 + FastSort(temp3) 
        print(a)
        return a   

__main()
