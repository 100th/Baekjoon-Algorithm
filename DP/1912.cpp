#include<iostream>
#include<cstdio>
using namespace std;

int arr[100001];
long long sumArr[100001];

long long max(long long a, long long b){
    if(a>b) return a;
    return b;
}

int main(void){
    int n;
    long long tmp;

    //입력
    cin >> n;
    for(int i=0; i<n; i++){
        scanf("%d", &arr[i]);
    }

    //계산
    sumArr[0] = arr[0];
    tmp = arr[0];
    for(int i=1 ;i<n; i++){
        sumArr[i] = max(sumArr[i-1] + arr[i], arr[i]);
        tmp = max(sumArr[i], tmp);
    }

    //출력
    cout << tmp;
    return 0;
}


출처: http://blockdmask.tistory.com/138 [개발자 지망생]
