public class Chapter11_class_member {
    // 클래스 멤버의 구분

    /*
    Python에서는 속성(attribute)라고 불리는 클래스 내부 요소가 Java에서는 멤버(member)라고 불리네.


    * 필드 구분 *

    1. 인스턴스 변수(instance variable)
     말 그대로 인스턴스 내부에 존재하며 인스턴스를 통해서만 호출할 수 있는 변수이다.

    2. 클래스 변수(class variable)
     인스턴스가 아닌 클래스 자체에서 호출할 수 있는 변수이다.
     인스턴스 변수와 다르게 static 제어자가 부여되어 있다.
    
    3. 지역 변수(local variable)
     메소드 내부에서 정의되는 변수이다.
     해당 변수를 외부에서 가져다 사용하는 것은 불가능하다.
    
    
    * 메소드 구분 *

    1. 인스턴스 메소드(instance method)
     말 그대로 인스턴스 내부에 존재하며 인스턴스를 통해서만 호출할 수 있는 메소드이다.

    2. 클래스 메소드(class method)
     인스턴스가 아닌 클래스 자체에서 호출할 수 있는 메소드이다.
     인스턴스 메소드와 다르게 static 제어자가 부여되어 있다.

    
    * 초기화 블록 *
    
    말 그대로 초기화를 실행하는 블록 부분이다.
    변수를 선언과 동시에 초기화하는, 명시적 초기화가 가능한 한편에 변수 선언 이후에 초기화의 순서를 세부적으로 조정할 때 쓰인다.
    중괄호만 쓰면 가능하고, 이때는 인스턴스 초기화 블록이 된다.
    근데 앞에 static 제어자를 부여하면 클래스 초기화 블록이 된다.

    */
}