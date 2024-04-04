#include <stdio.h>

int main() {
    // 표준 입출력
    char c1;
    puts("Input 1 : "); // 문자열을 그냥 출력하는 함수 / 자동 줄바꿈 좀 킹받네
    c1 = getchar(); // 문자 하나 입력받는 형식
    printf("%d %d %d\n", c1, c1+1, c1+2); // puts와 다르게 양식에 따라 출력을 진행

    // gets()는 deprecated되었다...
    getchar(); // c1 변수할당에서 입력받은 엔터를 무시하는 코드

    puts("Input 2 : ");
    char grade; int age;
    scanf("%c %d", &grade, &age);
    printf("등급 : %c, 나이 : %d\n", grade, age);

    // putchar()도 있는데 별로 안 쓸듯

    return 0;
}