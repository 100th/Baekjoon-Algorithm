#include <iostream>
#include <string>
using namespace std;

int main()
{
  int arr[5];
  int i, j, k;
  int sum = 0;
  arr[4] >= 0 ;
  arr[4] <= 100 ;
  arr[4] % 5 == 0 ;

  for ( i = 0 ; i <= 4 ; i++ ){
      cin >> arr[i];}

  for ( j = 0 ; j <= 4 ; j++ )
   {
    if ( arr[j] < 40 )
        arr[j] = 40;
    else
        continue;}

  for ( k = 0 ; k <= 4 ; k++ ){
  sum += arr[k];}

  cout << sum/5 << endl;

}
