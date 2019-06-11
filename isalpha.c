#include<stdio.h>
#include<string.h>
int main(){
  char a;
  scanf("%c",&a);
  if((a>=65&&a<=90)||(a<=122&&a>=97))
  printf("Alphabet");
  else
  printf("No");
}
