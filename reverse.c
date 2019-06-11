#include<stdio.h>
#include<string.h>
int main(){
  char a[100000];
  int i;
  scanf("%s",a);
  for(i=strlen(a)-1;i>=0;i--)
  putchar(a[i]);
}
