#include <iostream>
#include <string>
using namespace std;

int main(void)
{
	string str;

	for (int i = 0; i < 100 && !cin.eof(); i++)
	{
		getline(cin, str);
		cout << str << endl;
	}
/*
빈 줄이 주어질 수도 있고,
각 줄의 앞 뒤에 공백이 있을 수도 있다.
바로 앞 문제와 이 부분이 다르다.

!cin.eof()를 사용
*/
	return 0;
}
