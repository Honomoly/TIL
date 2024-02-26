public class Chapter02_type {
    public static void main(String[] args) {
        // 기본 타입(Primitive Type)
        // java의 기본타입에는 총 8종류가 존재한다

        // 1. 정수형 타입 : byte, short, int, long
        // byte : -2^7 부터 2^7-1까지 표현한다. 정확히 2^8개 (1바이트)
        byte num1 = 127;
        // short : -2^15 부터 2^15-1까지 표현한다. 정확히 2^16개 (2바이트)
        short num2 = 32767;
        // int : -2^31 부터 2^31-1까지 표현한다. 정확히 2^32개 (4바이트)
        int num3 = 2147483647;
        // long : -2^63 부터 2^63-1까지 표현한다. 정확히 2^64개 (8바이트)
        long num4 = 9223372036854775807L; // 뒤에 L 또는 l을 붙여야한다
        // 기본적으로 리터럴(우변)이 int형식이므로 

        // 2. 실수형 타입 : float, double
        // float : 4바이트의 단정도부동소수점(FP32) 양식을 따른다. 부호 1비트, 지수 8비트, 가수 23비트의 구성이다.
        float num5 = 439.112F; // 뒤에 F 또는 f을 붙여야한다
        // double : 8바이트의 배정도부동소수점(FP64) 양식을 따른다. 부호 1비트, 지수 11비트, 가수 52비트의 구성이다.
        double num6 = 439.112;
        
        /*
        long이나 float 변수 뒤에는 literal type suffix가 붙는 이유는 다음 챕터에서 설명한다.
        지수는 exponent, 가수는 fraction을 나타낸다
        */

        // 3. 문자형 타입 : char
        // char : 65536개(2바이트)의 문자를 표현하는 UNICODE 표현법을 따른다
        char str = '뎃';

        // 4. 논리형 타입 : boolean
        // boolean : 1비트만 있어도 될것 같지만 CPU가 읽을 수 있는 최소크기인 1바이트로 할당된다
        boolean bool = true;
    }
}
