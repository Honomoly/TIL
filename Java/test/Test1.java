package test; // 해당 클래스를 test라는 패키지 내부에 선언하는 코드

public class Test1 {
    public Test1() { // 여기는 public 안붙이니까 못찾네???
        System.out.println("Test1 클래스의 호출입니다");
    }
    // public을 붙이는 이유 : 제어자를 명시하지 않으면 default가 할당되는데, 이는 다른 패키지에서의 접근을 불허한다.

    public static void Test1StaticFunc() {
        System.out.println("Test1의 static method 호출입니다");
    }

    public void Test1InstanceFunc() {
        System.out.println("Test1의 instance method 호출입니다");
    }
}
