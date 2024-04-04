#include <stdio.h>

int main() {
    // c언어는 boolean 타입이 없고 1이 true, 0이 false으로 취급된다
    // 그래서 관계연산자의 결과가 0 또는 1이 나오게 된다

    // 연산자는 자바와 별 차이가 없는데, 비트연산만 정리는 해봄
    short a = 12; // 12은 이진법으로 ...00001100
    short b = 21; // 21은 이진법으로 ...00010101

    printf("%d\n", a&b);  // AND 연산 / ...00000100 (4)
    printf("%d\n", a|b);  // OR  연산 / ...00011101 (29)
    printf("%d\n", a^b);  // XOR 연산 / ...00011001 (25)
    printf("%d\n", ~a);   // NOT 연산 / ...11110011 (-13)
    printf("%d\n", a>>2); // 우 시프트 / ...00000011 (3)
    printf("%d\n", a<<2); // 좌 시프트 / ...00110000 (48)
    // 시프트 연산은 빈칸을 0으로 채워넣지만 음수의 경우 1을 집어넣어주긴 한다
    printf("%d\n", -2<<1);// 오류가 뜨긴 해도 값은 띄워준다

    return 0; // 실제로 return false의 효과와 동일하다
}