import myTools.Queue;

public class a_03_queue {
    public static void main(String[] args) {
        // 후입선출 : Last In First Out
        Queue queue = new Queue();
        System.out.println("Initial Length : " + queue.length);
        queue.push(1);
        queue.push(2);
        queue.push(3);
        System.out.println("Length After : " + queue.length);
        System.out.println(queue.pop());
        System.out.println(queue.pop());
        System.out.println(queue.pop());
        try {
            System.out.println(queue.pop());
        } catch (NullPointerException e) {
            System.out.println("Length : " + queue.length);
            System.out.println("이제 못나옵니다 ㅋㅋ");
        }
    }
}
