#include <iostream>
#include <string>
using namespace std;

int main()
{
  int n, count, answer, size;
  string ox;
  cin >> n ;
  cin.ignore();
// cin.ignore() : buffer 비워주기

  for ( int i = 0 ; i < n ; i++ )
    {
      count = 0, answer = 0;
      getline(cin, ox);
// getline 사용
      size = ox.size();

      for ( int j = 0 ; j < size ; j++)
        {
          if ( ox[j] == 'O')
            count++;
// 만약 O가 나온다면 count를 + 해라
          else
            count = 0;
          answer += count;
        }
        cout << answer << endl;
    }
  return 0;
}
