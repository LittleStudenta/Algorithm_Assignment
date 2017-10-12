template<class Type> 
int BinarySearch(Type a[], const Type& x, int l, int r)
{
     while (r >= l){ 
        int m = (l+r)/2;
        if (x == a[m]) return m;
        if (x < a[m]) r = m-1;  //在前半段
        else l = m+1; //在后半段
        }
    return -1;
} 
