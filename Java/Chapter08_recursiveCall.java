public class Chapter08_recursiveCall {
    // 재귀호출
    // Python에서는 극구 사용하지 않던 방법이다.
    public static int factorial(int num) {
        if (num > 1) {
            return num * factorial(num - 1);
        } else {
            return num >= 0 ? 1 : -1;
        }
    }

    public static void main(String[] args) {
        // 위에서 factorial 함수를 recursive call로 구현해보았다.
        System.out.println("6! = " + factorial(6));
        System.out.println("10! = " + factorial(10));
    }
}
