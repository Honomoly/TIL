package myTools;
import java.util.Stack;

class Node {
    public Node front;
    public Node rear;
    public Node parent;
    public int data;

    public Node(int x) {
        this.data = x;
        this.front = null;
        this.rear = null;
        this.parent = null;
    }
}



public class BinaryTree {
    public Node root;
    public int size;

    public BinaryTree() {
        this.root = null;
        this.size = 0;
    }

    public void push(int x) {
        if (this.size == 0) {
            this.root = new Node(x);
            this.size = 1;
        } else {
            boolean isFront = false;
            Node backup = null;
            Node pointer = this.root;
            while (!(pointer == null || pointer.data == x)) {
                backup = pointer;
                if (pointer.data > x) {
                    pointer = pointer.front;
                    isFront = true;
                } else {
                    pointer = pointer.rear;
                    isFront = false;
                }
            }
            if (pointer == null) {
                if (isFront) {
                    backup.front = new Node(x);
                } else {
                    backup.rear = new Node(x);
                }
                this.size++;
            } else {
                System.out.println("Value already exist!");
            }
        }
    }

    // class needed to cycling
    class stackItem {
        boolean toFront;
        Node node;

        stackItem(boolean toFront, Node node) {
            this.toFront = toFront;
            this.node = node;
        }
    }

    // 0 : in-order, 1 : pre-order, -1 : post-order
    public void show(int x) {
        if (this.size == 0) {
            return;
        } else {
            Node pointer = this.root;
            stackItem poped = new stackItem(true, pointer);
            boolean fromBottom = false;
            Stack<stackItem> stack = new Stack<>();

            stack.push(poped);

            while (stack.size() > 0) {
                if (fromBottom) {
                    if (poped.toFront) {
                        if (x == 0) System.out.print(poped.node.data + " ");
                        if (poped.node.rear != null) {
                            poped.toFront = false;
                            stack.push(poped);
                            pointer = poped.node.rear;
                            fromBottom = false;
                            continue;
                        }
                    }
                    if (x < 0) System.out.print(poped.node.data + " ");
                    poped = stack.pop();
                    continue;
                }

                // first arrival
                if (x > 0) System.out.print(pointer.data + " ");

                if (pointer.front != null) {
                    stack.push(new stackItem(true, pointer));
                    pointer = pointer.front;
                    continue;
                }

                if (x == 0) System.out.print(pointer.data + " ");
                
                if (pointer.rear != null) {
                    stack.push(new stackItem(false, pointer));
                    pointer = pointer.rear;
                    continue;
                }

                if (x < 0) System.out.print(pointer.data + " ");

                poped = stack.pop();
                fromBottom = true;
            }
        }
        System.out.println();
    }
}
