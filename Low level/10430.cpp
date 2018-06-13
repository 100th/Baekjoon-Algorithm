#include <iostream>
using namespace std;

int main()
{
  int A, B, C;
  A, B, C >= 2;
  A, B, C <= 10000;
  cin >> A >> B >> C;
  cout << (A + B) % C << endl;
  cout << (A % C + B % C) % C << endl;
  cout << (A * B) % C << endl;
  cout << (A % C * B % C) % C << endl;
  return 0;
}
