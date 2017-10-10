#include<stdio.h>
#include<iostream>
//没毛病啦，呜呼 

 int inside(int n,int multiplies,int *count ){
	if( n==-1 )                        
	    return 0;     
 	int multi=multiplies;
 	int countaa[10]={0};
	 
 	int ones=n%10;
 	int tens=n/10-1;         //这里减一也很好理解，体会一下 
 	int s=n/10;
 	int i,t=s;
 	//例317 先加310~317的各位 
 	for(i=0;i<=ones;i++){
	 	countaa[i]++;
	 	while(t){
	 		countaa[t%10]++;
	 		t=t/10;
	 	}	 
	 }
 	//再加0~310中的个位	
	for(i=0;i<10;i++)
 		countaa[i]+=s;
	for(i=0;i<10;i++)
		count[i]=count[i]+countaa[i]*multi;	
 	//再计算31中的各个位，出来乘以相应倍数	
 	inside(tens,10,count);
 	return 0;		
 }

 int main()
 {
    int count[10] = {0};
    int num=12345;
    inside(num,1,count);
    count[0]-=11;                    //这一行纠正了shit递归0多的问题 
    for(int i=0; i<10 ; i++)
        printf("%d\n",count[i]);    
    system("pause"); 
    return 0;
 }
