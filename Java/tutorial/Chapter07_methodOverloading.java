public class Chapter07_methodOverloading {

    public static void testMethod() {
        System.out.println("입력을 받지 않았습니다");
    }

    public static void testMethod(int integer) {
        System.out.println("정수를 입력받았습니다");
    }

    public static void testMethod(double float32) {
        System.out.println("실수를 입력받았습니다");
    }
    
    public static void main(String[] args) {
        // 메소드 오버로딩(method overloading)

        /*
         * 메소드 시그니쳐(method signature) : 메소드 선언부에 명시되는 매개변수의 리스트
        메소드 오버로딩이란 같은 이름의 메소드를 다른 메소드 시그니쳐를 가지고 중복해서 정의하는 것을 말한다.
        메소드 오버로딩이 되는 조건으로는 위의 정의한 문장 그대로 두 가지가 존재한다.
         1. 메소드명이 동일하다.
         2. 메소드 시그니쳐가 다른 구성(순서, 타입, 갯수등)을 가져야한다.
        */
        
        testMethod();
        testMethod(1);
        testMethod(3.14);

        // 아래와 같은 타입의 경우는 자동타입변환법에 따른다.
        testMethod(1f); // float -> double로 변환
        testMethod('a'); // char -> int로 변환
    }
}
