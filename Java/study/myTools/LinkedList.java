package myTools;
// 미완성
class Node {
    public int data;
    public Node prev;
    public Node next;

    public Node(int x) {
        this.data = x;
    }
}

public class LinkedList {
    private Node head;
    public int length;

    public LinkedList() {
        this.head = null;
        this.length = 0;
    }

    public LinkedList(int[] list) {
        this();
        int len = list.length;
        this.length = len;
        this.head = new Node(list[0]);
        Node pointer = this.head;
        for (int i = 1; i < len; i++) {
            pointer.next = new Node(list[i]);
            pointer.next.prev = pointer;
            pointer = pointer.next;
        }
        this.head.prev = pointer;
        pointer.next = this.head;
    }

    public void print() {
        Node pointer = this.head;
        for (int i = 0; i < this.length; i++) {
            System.out.print(pointer.data + " ");
            pointer = pointer.next;
        }
        System.out.println();
    }

    public int index(int x) {
        Node pointer = this.head;
        for (int i = 0; i < x; i++) {
            pointer = pointer.next;
        }
        return pointer.data;
    }

}
