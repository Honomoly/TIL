class ParentClass {
    // field
    public String common = "부모꺼";
    public String parent1 = "부모1";
    public String parent2;
    public String parent3;

    // initializer block
    {
        System.out.println("Step1");
        this.parent2 = "부모2";
    }

    // constructor
    ParentClass() {
        System.out.println("Step2");
        this.parent3 = "부모3";
    }

    // method
    public String getAllParent() {
        return parent1 + parent2 + parent3;
    }
}

class ChildClass extends ParentClass {
    // field
    public String common = "자식꺼";
    public String child1 = "자식1";
    public String child2;
    public String child3;

    // initializer block
    {
        System.out.println("Step3");
        this.child2 = "자식2";
    }

    // constructor
    ChildClass() {
        System.out.println("Step4");
        this.child3 = "자식3";
    }

    // method
    public String getAllChild() {
        return child1 + child2 + child3;
    }

    public String getAllFamily() {
        // this에서도 부모 요소 잘 불러온다.
        return this.getAllParent() + this.getAllChild();
    }

    public String getCommon() {
        // 부모와 자식 클래스중 서로 이름이 겹치는 요소가 있다면, 부모 요소는 super로 불러오면 된다.
        // this와 마찬가지로 인스턴스 메소드 내부에서만 사용할 수 있다.
        return super.common + this.common;
    }
}

public class Chapter12_inheritance {
    public static void main(String[] args) {
        ChildClass inst = new ChildClass();
        
        System.out.println("----");

        System.out.println(inst.parent1); // 부모 클래스의 멤버 잘 가져옴
        System.out.println(inst.getAllFamily());
        System.out.println(inst.getCommon());
    }
}