#include <stdio.h>
int main(void) {
	char str[30];
	int i,b,len;
	scanf("%s %d",&str,&b);
	len=strlen(str);
	for(i=b;i<len;i++)
	{
		printf("%c",str[i]);
	}
	return 0;
}
