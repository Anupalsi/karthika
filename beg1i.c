#include <stdio.h>

int main() {
	int a[10],K,i,N;
	int sum=0;
	scanf("%d %d",&N,&K);
	for(i=0;i<N;i++)
	 {
	  scanf("%d",&a[i]);
	 }
	 for(i=0;i<K;i++)
	 {
	 	sum=sum+a[i];
	 }
	printf("%d",sum); 
	return 0;
}
