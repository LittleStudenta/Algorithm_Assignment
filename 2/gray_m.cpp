#include<stdio.h>
#include<iostream>

int gray_m(int n,int *gray){
	if(n==0)
		return 0;
	else
		gray_m(n-1,gray);
	//然后干正事
	int a = 2^n;
	
	for(int i=0;i<a/2;i++)
		gray[i][n] = 0;	
	for(int i=a/2;i<a;i++){
		gray[i][n] = 1;
		for(int j=0;j<n;j++)
			gray[i][j] = gray[a-i-1][j];
	}
				
}

int main(){
	int num = 3;
	int a = 2^n;
	int grayma[a][n]={0};
	gray_m(num,grayma);
	
	for(int j=0;j<a;j++){
			for(int i=0;i<n;i++)
			
			printf(" %d",grayma[j][i]);
		printf("/n");
	}
		
} 