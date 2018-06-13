#include<iostream>
using namespace std;

int main(void)
  {
    int y[10001];
    int z[10001];
// y와 z를 10001까지 배열로 만든다.
    int n, x;
    int j = 0;
    cin >> n >> x ;
    for ( int i = 1 ; i <= n ; i++ )
    {
      cin >> y[i];
  // n의 개수 만큼 입력 할 것이다
      if ( y[i] < x )
  // x보다 작은 수를 출력할 것이다
      {
        z[j] = y[i];
  // 그렇게 선별한 y배열을 z[j]배열로 할당한다
        j++;
  // j를 하나씩 늘려가면서
      }
     }
     for (int i = 0 ; i < j ; i++ )
        cout << z[i] << " " ;
  // 그렇게 뽑아진 j들만 z배열에서 출력한다
  }
