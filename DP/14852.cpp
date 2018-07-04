// D[i] = 3 * D[i-2] + 2 * D[i-1] + (2 * D[i-3] + 2 * D[i-4] ... 2 * D[0])
// 2씩 더해지는 부분을 처리하기 위해 배열에 별도의 행을 만들어 처리

#include <iostream>
using namespace std;

long long int d[1000001][2];

long long int dp(int x) {
  d[0][0] = 0;
  d[1][0] = 2;
  d[2][0] = 7;
  d[2][1] = 1;
  for(int i = 3; i <= x; i++){
    d[i][1] = (d[i-1][1] + d[i-3][0]) % 100000007;
    d[i][0] = (3 * d[i-2][0] + 2 * d[i-1][0] + 2 * d[i][1]) % 100000007;
  }
  return d[x][0];
}

int main(void)
{
  int x;
  cin >> x;
  cout << dp(x) << endl;
  return 0;
}
