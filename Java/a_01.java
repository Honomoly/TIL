import java.io.IOException; // 이거 안하면 java는 터미널 입력이 불가능하게 구성해두었다

public class a_01 {
    public static void main(String[] args) throws IOException {
        /*
        기본적으로 터미널에서 값을 입력한 후 Enter을 누르게 된다면, 입력값과 개행(줄바꿈, 코드 10)이 입력이 된다.
        그래서 아래의 예제에서는 복수의 입력을 받는 경우, 입력 갯수를 정확하게 입력하는 것이 좋다.
        */

        // System.out.print("Input : ");
        // int input1 = System.in.read();
        // System.out.println("Output : " + input1);

        // System.out.println("------");
        // System.in.read(); // 개행(10)을 대신 입력받는 코드

        System.out.print("Input : ");
        byte[] input2 = new byte[7];
        System.in.read(input2);

        System.out.print("Output(ASCII) : ");
        for (int i = 0; i < input2.length; i++) {
            System.out.print(input2[i] + " ");
        }
        System.out.println();

        String str = new String(input2);
        System.out.println("Output(String) : " + str);
        System.out.println("Output(String.trim()) : " + str.trim());
        // trim() : 문자열 양 끝에서부터 아스키코드 20이하의 공백을 모두 제거한다.
        // strip() : 문자열 양 끝에서부터 유니코드의 공백을 모두 제거한다. (예 : \u2003)
        int num = Integer.parseInt(str.trim());
        System.out.println("Output(Integer) : " + num);
    }
}
