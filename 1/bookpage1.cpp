#include<stdio.h>
#include<iostream>
//ûë�������غ� 

 int inside(int n,int multiplies,int *count ){
	if( n==-1 )                        
	    return 0;     
 	int multi=multiplies;
 	int countaa[10]={0};
	 
 	int ones=n%10;
 	int tens=n/10-1;         //�����һҲ�ܺ���⣬���һ�� 
 	int s=n/10;
 	int i,t=s;
 	//��317 �ȼ�310~317�ĸ�λ 
 	for(i=0;i<=ones;i++){
	 	countaa[i]++;
	 	while(t){
	 		countaa[t%10]++;
	 		t=t/10;
	 	}	 
	 }
 	//�ټ�0~310�еĸ�λ	
	for(i=0;i<10;i++)
 		countaa[i]+=s;
	for(i=0;i<10;i++)
		count[i]=count[i]+countaa[i]*multi;	
 	//�ټ���31�еĸ���λ������������Ӧ����	
 	inside(tens,10,count);
 	return 0;		
 }

 int main()
 {
    int count[10] = {0};
    int num=12345;
    inside(num,1,count);
    count[0]-=11;                    //��һ�о�����shit�ݹ�0������� 
    for(int i=0; i<10 ; i++)
        printf("%d\n",count[i]);    
    system("pause"); 
    return 0;
 }
