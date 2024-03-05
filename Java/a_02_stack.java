import myTools.Stack;

public class a_02_stack {
    public static void main(String[] args) {
        // 후입선출 : Last In First Out
        Stack stack = new Stack();
        System.out.println("Initial Length : " + stack.length);
        stack.push(1);
        stack.push(2);
        stack.push(3);
        System.out.println("Length After : " + stack.length);
        System.out.println(stack.pop());
        System.out.println(stack.pop());
        System.out.println(stack.pop());
        try {
            System.out.println(stack.pop());
        } catch (NullPointerException e) {
            System.out.println("Length : " + stack.length);
            System.out.println("이제 못나옵니다 ㅋㅋ");
        }
    }
}
