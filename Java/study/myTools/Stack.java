package myTools;

class StackData {
    public int data;
    public StackData below; // 이게 되네? 하긴 재귀도 되는데

    {
        this.below = null;
    }

    StackData(int x) {
        this.data = x;
    }
}

public class Stack {
    public int length;
    private StackData top; // 마지막으로 들어온 데이터이자 나가야할 데이터

    public Stack() {
        this.length = 0;
        this.top = null;
    }

    public void push(int x) {
        StackData newData = new StackData(x);
        newData.below = this.top;
        this.top = newData;
        this.length += 1;
    }

    public int pop() {
        int data = this.top.data;
        this.top = this.top.below;
        this.length -= 1;
        return data;
    }
}
