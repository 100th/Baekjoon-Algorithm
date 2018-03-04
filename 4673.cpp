#include<iostream>
using namespace std;
const int N = 10001;
/*
여기서 const를 함으로써, 절대로 N 값이 바뀌지 않게 해준다.
def로 정의하는 방법도 있는데, const가 더 쉽고 일반적이다.
*/
bool arr[N];
int solution(int n){
// 처음 나온 함수 만들어서 풀기
    int sum = n;
    while( n != 0 ){
// for 뿐만 아니라 while 도 잘 이용해야 한다.
// n이 0이 아닐 때 까지 돌린다.
        if(n == 0)
          break;
// 만약 n이 0이면 멈춘다.
        sum += n % 10;
        n = n / 10;
     }
    return sum;
}
int main(void){
    for(int i=1; i<N; i++){
        int idx = solution(i);
// solution 함수 불러오기
        if(idx <= N){
            arr[idx] = true;
// true를 준다.
        }
    }
    for(int i=1; i<N; i++){
        if(!arr[i])
        cout << i << endl;
    }
    return 0;
}
