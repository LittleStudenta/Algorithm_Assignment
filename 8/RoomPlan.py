  
def __main():
    b = open('F:\\_Algorithm_Assignment\\8\\input.txt')
    n = int(next(b))
    a = [0]*n
    for i in range(n) :
        c = next(b)[0:-1]
        a[i] = [int(i) for i in c.split(' ')] 
   
    print(RoomPlans(a, n))
    c = 1

def RoomPlans(a, n):
    a = EndTimeSort(a)
    rooms = []
    k = 0
    for i in range(n):
        if i == 0:
            rooms.append([a[i]])
        else:  
            rooms = DescendOrderRooms(rooms)  
            for num in range(len(rooms)+1):   
                if num == len(rooms):
                    rooms.append([a[i]])
                elif a[i][0] >= rooms[num][-1][1]:
                    rooms[num].append(a[i])
                    break
                else:
                    continue
                  
                  
    return len(rooms)
    
def EndTimeSort(a):
    length = len(a)
    if length <= 1 :
        return a
    else:
        flag = (length-1)//2
        temp1, temp2, temp3 = [], [], []
        for i in range(length):
            if a[i][1] < a[flag][1]:
                temp1.append(a[i])
            elif a[i][1] == a[flag][1]:
                temp2.append(a[i])
            else:
                temp3.append(a[i])     

        a = EndTimeSort(temp1) + temp2 + EndTimeSort(temp3) 
        print(a)
        return a   

def DescendOrderRooms(rooms):
    length = len(rooms)
    if length <= 1 :
        return rooms
    else:
        flag = (length-1)//2
        temp1, temp2, temp3 = [], [], []
        for i in range(length):
            if rooms[i][-1][1] < rooms[flag][-1][1]:
                temp1.append(rooms[i])
            elif rooms[i][-1][1] == rooms[flag][-1][1]:
                temp2.append(rooms[i])
            else:
                temp3.append(rooms[i])     

        rooms = DescendOrderRooms(temp3) + temp2 + DescendOrderRooms(temp1) 
      
        return rooms 




__main()
