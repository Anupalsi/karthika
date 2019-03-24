#include <stdio.h>

int main(void) {
	int N,i,j,a[10];
	scanf("%d",&N);
	for(i=0;i<N;i++)
	{
		scanf("%d",&a[i]);
	}
	for(i=0;i<N;i++)
	{
		for(j=i+1;j<N;j++)
		{
			if(a[i]==a[j])
		{
			printf("%d\t",a[i]);
		}
		}
	}
	return 0;
}
