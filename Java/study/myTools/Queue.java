package myTools;

class QueueData {
    public int data;
    public QueueData next;

    {
        this.next = null;
    }

    QueueData(int x) {
        this.data = x;
    }
}

public class Queue {
    public int length;
    private QueueData front; // 먼저 들어온 데이터 / 곧 나가야 함
    private QueueData rear; // 마지막으로 들어온 데이터 / 뒤에 따라 들어오는 곳이 있음

    public Queue() {
        this.length = 0;
        this.front = null;
        this.rear = null;
    }

    public void push(int x) {
        // 뒤에다 데이터 붙이기
        if (length == 0) {
            this.rear = new QueueData(x);
            this.front = this.rear;
        } else {
            this.rear.next = new QueueData(x);
            this.rear = this.rear.next;
        }
        this.length += 1;
    }

    public int pop() {
        // 앞에서 데이터 빼내기
        int data = this.front.data;
        this.front = this.front.next;
        this.length -= 1;
        if (this.length == 0) {
            this.rear = null;
        }
        return data;
    }
}
