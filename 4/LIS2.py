
def __main():
    a = [1,2,24,7,4,5,1,6,7,10,9,6,56,23,4,53,9]
    print( Max_rise(a) )

def Max_rise(a):
   
    length = len(a)
    maxlist = [0]*length

    for i in range(0,length): #找出每个第i个结尾的子序列    
        if i == 0:
            maxlist[i] = 1
            continue
        m = shit(a,maxlist, i-1, a[i])
        maxlist[i] = maxlist[m] + 1  
    
    finallist = []
    j = length-1
    while j > 0 :
        if maxlist[j] == max(maxlist):
            finallist.append( a[j] )
            break
        else:
            j -=1

    while j > 0: 
        m = shit(a, maxlist, j-1, a[j])   
        finallist.append( a[m] ) 
        j = m  
    finallist.reverse()
    return finallist

def shit(a,b,i,e):  #找b中i以内比e小最长的子序列的结尾,return位置
    
    c = b[0:i+1]
    j, k = 0, i
    while j != k:
        if a[j] <= e: 
            if a[k] <= e :
                if b[k] > b[j]:
                    j += 1
                    continue
                else:
                    k -= 1
                    continue
            else:
                k -= 1
        else:        
            j += 1                
    return j

__main()


























