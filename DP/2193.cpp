#include <stdio.h>

int N;
long output[100];

int main(){

  scanf("%d", &N);

  for (int i = 1; i <= 91 ; i++){
    output[1] = 1;
    output[2] = 1;

    output[i] = output[i-1] + output[i-2];
  }
  printf("%ld\n", output[N]);
}
