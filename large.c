#include<stdio.h>

int main(){
  int i,a,max=-30000;
  for(i=0;i<3;i++){
    scanf("%d",&a);
    max=a>max?a:max;
  }
  printf("%d",max);
}
