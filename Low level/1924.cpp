#include<iostream>
using namespace std;

int main()
  {
    int month[12] = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
    char week[7][4] = {"MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"};
    int x, y, i;
    int day;
/*
month에 [12]로 12개를 만든다. 각 month별로 며칠까지 있는지
week를 [7][4]로 만들어서 matrix를 만든다.
*/
    cin >> x >> y;

    for ( i = 1 ; i < x ; i++ )
    {
      day = day + month[i-1];
    }
    day = day + y - 2;

    cout << week[day % 7] ;
  }
