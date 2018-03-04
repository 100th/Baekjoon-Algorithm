#include<iostream>
#include<string>
using namespace std;

string s;

int main()
  {
    cin >> s;
    for(int i = 0 ; i < s.size() ; i++)
      {
        cout << s[i];
        if( i % 10 == 9 )
        {
          cout << endl;
// 10글자씩 끊어서 출력하기
        }
    }
}
