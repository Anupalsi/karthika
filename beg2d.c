#include <stdio.h>

int main(void) {
	int a,i,b;
	scanf("%d %d",&a,&b);
	for(i=a+1;i<b;i++)
	{
		if(i%2!=0)
		printf("%d\t",i);
	}
	return 0;
}
