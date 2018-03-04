#include <iostream>
#include <string>
using namespace std;
int main()
{
string k;
int cnt = 0;
int getSize = 0;
int isThereAlpha = 0;
int first = -1;
/*
문자조작함수 :
1. isalpha : 알파벳이니?
2. isupper : 대문자니?
3. islower : 소문자니?
4. isdigit : 숫자니?
5. toupper : 대문자로
6. tolower : 소문자로
*/
getline(cin, k); // getline(cin, str)
for (int num = 0; num < k.size(); num++)
// .size() = .length() 단어 크기 물어보는
  {
    if (isalpha(k[num]) ) // 알파벳이니?
      {
        isThereAlpha = num;
        first++;
        break;
      }
    }
    if (first == -1)
      {
        cout << "0";
        return 0;
      }
for (int i = isThereAlpha; i < k.size(); i++)
    {
      if ( k[i] == ' ' && isalpha(k[i + 1]))
      cnt++;
      continue;
      if (i + 1 > k.size())
      break;
     }
    cout << cnt + 1;
}
