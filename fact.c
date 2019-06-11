#include<stdio.h>
long long fact(int a)
{
	if(a>1)
	return a*fact(a-1);
	return 1;
}
int main(){
  int a;
  scanf("%d",&a);
  printf("%lld",fact(a));
}
