#include <iostream>
#include <string>
using namespace std;

int main()
{
  string A;
  while (true)
  {
    getline(cin, A);
    if (A == "" || A.empty() || A == "\n")
      break;
    cout << A << endl;
  }
/*
문제가 입력받은 그대로 출력해야 한다.
각 줄은 공백으로 시작하지 않고,
공백으로 끝나지 않는다는 조건이다.
빈 줄도 없다.
*/
  return 0;
}
