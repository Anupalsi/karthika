#include <stdio.h>

int main(void) {
	int a,i,count=0;
	scanf("%d",&a);
	for(i=2;i<a;i++)
	{
		if(a%i==0)
	    count++;
	}
	if(count==0)
		printf("yes");
    else
		printf("no");
	return 0;
}
