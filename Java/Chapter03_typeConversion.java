public class Chapter03_typeConversion {
    public static void main(String[] args) {
        // 타입 변환(Type Conversion)
        // 1. Implicit Conversion
        // 대입, 산술연산에서 자동으로 이루어지는 타입 변환이다.
        double num1 = 10; // 타입은 double인데 리터럴은 int이니 알아서 변환해서 대입연산
        // int num2 = 3.14; // 정수에 실수를 넣는 대입연산 -> 이건 손실이 일어나므로 오류난다!
        double num3 = 7.0f + 3.14; // 7.0f은 float이지만 알아서 double로 변환해서 계산하는 산술연산

        /*
        * Conversion Hierarchy *
        byte → short → int → long → float → double
                char ↗

        long이나 float 변수 뒤에는 literal type suffix가 붙는 이유 :
        정수타입 변수에 입력되는 리터럴(우변에 기입하는 명시적인 숫자)은 변수에 할당되기 전에는 메모리에 int형식을 기본값으로 하여 임시저장된다.
        마찬가지로 실수타입의 리터럴은 메모리에 double형식을 기본값으로 임시저장된다.
        그러므로 int범위를 벗어난 숫자는 메모리에 임시저장하는 단계부터 숫자 뒤에 L(l) 접미사를 붙여 메모리에 long형식으로 저장하게 된다.
        또한 범위 내에 존재하기만 하면 byte나 short에는 int형식의 숫자가 자동으로 대입연산되기 때문에 뒤에 아무 접미사도 붙일 필요가 없다.

        하지만, 아쉽게도 float에는 이러한 자동 대입연산을 할 수 없다.
        분명 float이 표현할 수 있는 값으로 보인다 해도 double 변수가 float변수로 자동 대입연산될 수는 없다는 말이다.
        왜냐하면 실제로 따져보면 똑같은 숫자가 아니기 때문에 대입 과정에 손실이 일어나게 된다.
        그래서 float은 미리 뒤에 F(f) 접미사를 붙여 메모리에 임시저장해야 한다.
        */

        // 2. Explicit Conversion
        // 바꿀 타입일 지정하는 강제적인 타입 변환이다.
        // float num4 = num1/num3; // 이러면 오른쪽은 double이므로 float인 num3에 대입할 수 없다.
        float num4 = (float) (num1/num3); // 명시적으로 타입을 float으로 변환하면 대입이 가능해진다.
        System.out.println(num4);
    }
}
