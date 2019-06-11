#include <stdio.h>


int main(void) {
	long int n,i,j,k=0;
	scanf("%ld",&n);
	int a[n];
	for(i=0;i<n;i++){
		scanf("%ld",&a[i]);
		k=k^a[i];
	}
	printf("%d",k);
	return 0;
}
