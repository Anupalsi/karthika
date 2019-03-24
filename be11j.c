//anukarthika
#include <stdio.h>

int main(void) {
	int num,num1,c=1,i;
	scanf("%d %d",&num,&num1);
	for(i=1;i<=num1;i++)
	{
		c=c*num;
	}
	printf("%d",c);
	return 0;
}
