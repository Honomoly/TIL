#include <stdio.h>

// 지금까지 배웠던거 활용해보기

// 이전에 Python에서 만들었던 소수계량 함수를 C언어로 구현해보자

int pi_function(int N) {
    if (N < 2) return 0;
    else if (N == 2) return 1;

    int seq[N];
    int *ptr1 = seq, *ptr2 = seq, *ptr3, num;

    for (int i = 2; i <= N; ++i) {
        ++ptr2;
        *ptr2 = i;
    }
    *ptr1 = 0;

    int *end = ptr2 - 1;
    ptr2 = seq + 1;

    while ((*ptr2)*(*ptr2) <= N) {
        *ptr1 = *ptr2;
        ptr3 = ptr2;
        num = *ptr2;
        while (ptr3 <= end) {
            if (*ptr3 != 0) *ptr3 = 0;
            ptr3 += num;
        }
        ++ptr1;
        while (*ptr2 == 0) ++ptr2;
    };

    int result = 0;
    ptr1 = seq;
    
    for (int i = 1; i <= N; ++i) {
        if (*ptr1 != 0) ++result;
        ++ptr1;
    }

    return result;
}

int main() {
    int input;
    printf("Input Value : ");
    scanf("%d", &input);
    printf("Value of pi(%d) : %d\n", input, pi_function(input));
    return 0;
}