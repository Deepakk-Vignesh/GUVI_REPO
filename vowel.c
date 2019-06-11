#include<stdio.h>
int main(){
  char a;
  scanf("%c",&a);
  if((tolower(a)<65&&tolower(a)>90))
  printf("invalid");
  else
  if(tolower(a)=='a'||tolower(a)=='e'||tolower(a)=='i'||tolower(a)=='o'||tolower(a)=='u')
  printf("Vowel");
  else
  printf("Consonant");
}
