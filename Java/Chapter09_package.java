import test.Test1; // 패키지 내부에 선언된 클래스를 import

public class Chapter09_package {
    public static void main(String[] args) {
        Test1.Test1StaticFunc();

        System.out.println("----");

        Test1 inst = new Test1();
        inst.Test1InstanceFunc();
    }
}
