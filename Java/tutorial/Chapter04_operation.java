// 클래스 만들어두기
class ClassA {};
class ClassB extends ClassA {}; // A 클래스 상속 받음

public class Chapter04_operation {
    public static void main(String[] args) {
        // 1. 산술 연산
        // +, -, *, /, % 개념은 다른 언어와 동일
        byte num1 = 21, num2 = 7;
        System.out.println(num1 + num2);
        System.out.println(num1 - num2);
        System.out.println(num1 * num2);
        System.out.println(num1 / num2); // 근데 여기는 둘다 byte인지라 결과도 byte로 나오게 된다
        System.out.println(num1 % num2);

        System.out.println("--1--");


        // 2. 대입 연산
        // =, +=, -=, *=, /=, %= 같은 복합연산도 모두 가능


        // 3. 증감 연산
        // 앞에 붙으면 전위, 뒤에 붙으면 후위연산이다.
        // 연산의 기준은 해당 증감 연산을 상위 연산을 시행하기 전에 할지, 상위 연산 실행 후에 할지 정한다.


        // 4. 논리 연산
        // 누구나 다 아는 AND(&&), OR(||) 연산을 가지고 있다.


        // 5. 비트 연산
        // 말 그대로 bitwise operation이다
        // 21과 7은 2진법(byte형식)으로 00010101, 00000111이다.
        System.out.println(num1 & num2); // AND : 00000101(5)
        System.out.println(num1 | num2); // OR  : 00010111(23)
        System.out.println(num1 ^ num2); // XOR : 00010010(18)
        System.out.println(~num1);       // NOT : 11101010(-22)

        System.out.println("--2--");

        byte num3 = (byte) ~num1; // 11101010(-22) : 음수 하나 만들기

        // 비트를 좌우로 움직이는 비트 시프트 연산(<<, >>) 또한 존재한다.
        // 왼쪽의 경우 빈 곳을 0이 채우게 된다. 그러다보니 양수든 음수든 값이 2의 배수형태로 뛰는 효과가 있다.
        System.out.println(num1 << 1); // 00101010(42)
        System.out.println(num3 << 1); // 11010100(-44)

        // 오른쪽의 경우 양수면 0, 음수면 1이 채우게 된다. 이러한 방식으로 부호가 유지되는 비트 시프트가 된다.
        // 효과는 2n -> n, 2n+1 -> n 의 형식을 따르게 된다.
        System.out.println(num1 >> 1); // 00001010(10)
        System.out.println(num3 >> 1); // 11110101(-11)

        System.out.println("--3--");

        // 다만 기호를 3번 사용하는 오른쪽 비트 시프트(>>>)는 무조건 새 비트를 0으로 채운다.
        // 그렇다보니 음수의 경우 값이 역변한다
        System.out.println(num1 >>> 1); // 00001010(10)
        System.out.println(num3 >>> 1); // 11110101(??) : 메모리에는 int로 저장이 되기에 값이 조금 괴랄하다.

        System.out.println("--4--");


        // 6. 기타 연산
        // 유일한 삼항 연산
        System.out.println(num1 > num2 ? "Yeah" : "Nope"); // JavaScript와 동일하다.

        System.out.println("--5--");

        // python의 isinstance 메소드와 동일한 효과를 가지는 연산
        // 맨 위에서 만든 클래스로 인스턴스 생성
        ClassA instA = new ClassA();
        ClassB instB = new ClassB();
        System.out.println(instA instanceof ClassA);
        System.out.println(instB instanceof ClassA); // ClassB가 ClassA를 부모 클래스로 가지고 있으므로 여기는 참이다
        System.out.println(instA instanceof ClassB); // 당연히 이건 안된다
        System.out.println(instB instanceof ClassB);
    }
}
