#include<stdio.h>
int main(){
  char a;
  scanf("%c",&a);
  if((a<65&&a>90)||(a>122&&a<97))
  printf("invalid");
  else
  if(tolower(a)=='a'||tolower(a)=='e'||tolower(a)=='i'||tolower(a)=='o'||tolower(a)=='u')
  printf("Vowel");
  else
  printf("Consonant");
}
