#include <stdio.h>


int main(void) {
	long int n,i,j,k=0;
	scanf("%ld",&n);
	int a[n];
	for(i=0;i<n;i++){
		scanf("%ld",&a[i]);
		if(i==a[i]){
			k++;
			printf("%d ",a[i]);
		}
	}
	if(k==0)
	printf("-1");
	return 0;
}
