// generic : 데이터 타입을 일반화하는 문법
// 클래스를 일반적으로 정의하여 클래스를 좀 더 범용적으로 사용할 수 있게 해준다
class TestClass<cls> {
    // cls로 데이터 타입을 일반화 하였다. 이를 type variable이라고 부른다
    private cls var;

    TestClass() {
        var = null;
    }

    TestClass(cls x) {
        var = x;
    }

    public cls get_var() {
        return this.var;
    }

    // 제네릭 메소드 : 클래스에서 했던 짓과 똑같은 일을 할 수 있다
    // 근데 여기의 cls는 위의 cls와는 별개의 것이다!
    public static <cls> void get(cls x) {
        System.out.println(x);
    }
}

public class Chapter13_generic {
    public static void main(String[] args) {
        // TestClass a = TestClass(); // 제네릭을 명시 안하면 오류난다
        TestClass<Integer> b = new TestClass<Integer>(4);
        System.out.println(b.get_var());
        TestClass<String> c = new TestClass<String>("yes");
        System.out.println(c.get_var());
        TestClass<String> d = new TestClass<>("no"); // 타입 추정이 가능하면 그냥 생략해도 됨 
        System.out.println(d.get_var());
        TestClass<?> e = new TestClass<>(); // 와일드 카드를 이따구로 사용하는 방법도 있다
        System.out.println(e.get_var());

        TestClass.get("뭐요");
        TestClass.get(61);
    }
}
