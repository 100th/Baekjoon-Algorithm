#include<iostream>
using namespace std;

int main(void)
  {
    int n;
    cin >> n;

    int max = 0;
    float sum = 0;

    int score[1000];

    for (int i = 0; i < n; i++)
    {
      cin >> score[i];
      if (max < score[i])
          max = score[i];
    }
  for (int j = 0; j < n ; j++)
    sum += ((float)score[j] / max)* 100;

  cout << sum/n ;
}
