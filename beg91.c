#include <stdio.h>

int main(void) {

	int L,B,H,vol,tsa;
	scanf("%d %d %d",&L,&B,&H);
	vol=L*B*H;
	tsa=(2*((L*B)+(B*H)+(H*L)));
	printf("%d %d",tsa,vol);
	return 0;
}
