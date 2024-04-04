// 클래스명은 여타 언어와 마찬가지로 대문자로 시작하며 카멜표기법을 따르는 것이 관례다.
// 외부 파일에서 실행하기 위해서는 파일명과 클래스명을 동일하게 만들어야만 한다!
public class Chapter00_start {
    /*
    클래스 내부에는 반드시 메소드가 하나 존재해야 한다.
    근데 없어도 클래스명과 동일한 메소드(생성자)가 자동 생성되니 신경 ㄴㄴ.

    밑은 파일 실행시 자동으로 실행되는 클래스 메소드(static method)이다.
    반드시 메소드명을 main()으로 정의해야만 java가 이를 찾아서 실행해준다!
    */
    public static void main(String... args) {
        // 그냥 print는 줄바꿈 없다
        System.out.print(3);
        System.out.println(6);
        System.out.println(9);

        // 문자열 덧셈도 그대로
        System.out.println("이건 파이썬이랑 " + "동일하다");

        // 근데 숫자열과 문자열 덧셈은 뭐냐
        System.out.println("파이썬은 이런거 안됨 " + 999);
    }
}