// Class

// 자바의 클래스는 파이썬, 자바스크립트 개념과 거의 동일하다고 보면 된다.

// 클래스 선언
class Car { // 클래스명
    // 필드(field)
    // 인스턴스가 가지는 변수이다
    private String modelName;
    private int modelYear;
    private boolean __isMyCar;
    private int currentVelocity;

    /* 참고 *
    public과 private은 접근 제어자라고 하며 기능은 다음과 같다.
    public : 해당 속성을 객체 외부에서 우리가 잘 아는 '그 방식'으로 자유롭게 호출할 수 있다.
    private : 내부에 있는 변수나 메소드에서만 this을 이용하여 호출이 가능하다.
    */

    // 생성자(constructor)
    // 인스턴스가 생성될 때 실행할 작업을 표시하며 '반드시' 클래스명과 동일해야 한다.
    // 반환값이 존재하지 않지만 void형으로 선언하지 않는다.
    // 생성자는 복수로 존재하는 것이 가능하다.
    Car(String modelName, int modelYear) {
        // this : 인스턴스 메소드 내부에서 인스턴스 자기 자신을 참조하는데 사용하는 변수
        this.modelName = modelName;
        this.modelYear = modelYear;
        this.__isMyCar = false;
        this.currentVelocity = 0;
    }

    Car(String modelName, int modelYear, boolean isMyCar) {
        this.modelName = modelName;
        this.modelYear = modelYear;
        this.__isMyCar = isMyCar;
        this.currentVelocity = 0;
    }

    Car() {
        // this() : 생성자 내부에서 다른 생성자를 호출할 때 사용하는 메소드
        // 반드시 첫 줄에서만 호출할 수 있다.
        this("정보없음", 0);
    }

    // 메소드(method)
    // 접근제어자, 반환타입, 메소드명 순서로 입력한다
    public String getModel() {
        return this.modelYear + "년식 " + this.modelName;
    }

    public void isMyCar() {
        if (this.__isMyCar) {
            System.out.println("차를 소유한 상태입니다.");
        } else {
            System.out.println("차를 소유하지 않은 상태입니다.");
        }
        
    }

    public void accelerate(int delta) { // 매개변수 받는 것은 당연히 가능
        this.currentVelocity += delta;
        if (this.currentVelocity < 0) {
            this.currentVelocity = 0;
        } else if (this.currentVelocity >= 200) {
            this.currentVelocity = 200;
            System.out.println("한계 속도 200km/h에 도달했습니다.");
            return;
        }
        System.out.println("현재 속도는 " + this.currentVelocity + "km/h입니다.");
    }
}

public class Chapter06_class {
    public static void main(String[] args) {
        // 위에서 생성한 클래스로 인스턴스 생성
        Car genesis; // 일단 참조변수 선언
        genesis = new Car("제네시스", 2020); // 인스턴스 생성
        System.out.println(genesis.getModel()); // 이제 내부 메소드 사용 가능
        genesis.isMyCar();

        System.out.println("----");

        Car sonata = new Car("소나타", 2018, true); // 근데 한 줄에 하는 것도 가능하네
        System.out.println(sonata.getModel());
        sonata.isMyCar();

        System.out.println("----");

        genesis.accelerate(30);
        genesis.accelerate(60);
        genesis.accelerate(90);
        genesis.accelerate(50);

        System.out.println("----");

        Car emptyCar = new Car();
        System.out.println(emptyCar.getModel());
    }
}
