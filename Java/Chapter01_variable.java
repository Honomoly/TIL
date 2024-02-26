public class Chapter01_variable {
    public static void main(String[]  args) {
        // 아래 변수들은 System.out.println()으로 얼마든지 출력 가능

        // 변수 선언
        int num; // 이 상태에는 아무것도 없음
        num = 2;

        // 동시 선언
        int num1, num2; // 같은 타입의 변수를 동시에 선언함.
        // num1 = 5, num2 = 7; 근데 동시에 초기화는 불가
        num1 = 5; num2 = 7;
        double num3 = 3.14; // 선언과 동시에 초기화함.
        double num4 = 1.23, num5 = 4.56; // 같은 타입의 변수를 동시에 선언하면서 초기화함.

        // 상수(constant) 선언법
        // 상수는 대문자로 표기하는 것이 관례다
        final int NUM6 = 8;
    }
}