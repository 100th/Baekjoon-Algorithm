#include <iostream>
using namespace std;

int main()
{
  int exam;
  exam >= 0, exam <= 100;
  cin >> exam ;

  if ( exam >= 90)
    cout << "A" << endl;
  else if (exam >= 80)
    cout << "B" << endl;
  else if (exam >= 70)
    cout << "C" << endl;
  else if (exam >= 60)
    cout << "D" << endl;
  else
    cout << "F" << endl;

  return 0;
}
