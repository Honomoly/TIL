public class Chapter10_modifier {
    // 제어자(modifier)

    /*
    클래스나 클래스의 속성(attribute)을 선언할 시 부여하는 키워드다.
    제어자에는 접근 제어자(access modifier)와 그 외의 제어자가 존재한다.


    * 접근 제어자 *

    접근 제어자는 클래스의 속성(필드, 메소드)에 부여하는 제어자로, 말 그대로 접근할 수 있는 범위를 제어하는 기능이다.
    접근 제어자에는 4종류가 존재한다.

    1. private
     외부에서의 접근을 완전히 차단하며 오로지 클래스의 내부 메소드로만 접근할 수 있다.

    2. public
     외부에서의 접근을 완벽하게 허용하며 해당 객체를 사용하는 멤버라면 어디서나 접근할 수 있다.
     참고로 클래스에도 부여할 수 있는 제어자이다.
  
    3. default
     같은 패키지 내부에 있는 멤버에서만 접근을 허용하며 다른 패키지에서의 접근을 불허한다.
     제어자가 지정되지 않으면 기본적으로 할당되는 제어자이다.

    4. protected
     default와 비슷하지만 추가적으로 자식 클래스 관련 허용이 존재한다. 
     즉, 외부 패키지에 있더라도 해당 클래스를 상속받은 자식 클래스에서는 접근을 허용한다.

    허용 범위를 일렬로 세우면 다음과 같다.
    public > protected > default > private


    * 기타 제어자 *
    
    1. final
     클래스, 메소드, 필드, 지역변수(local variable)에 부여 가능한 제어자이다.
     이 제어자는 '변경할 수 없다'는 의미로 사용된다. 다시 말해, 값을 변경되지 않는 상수를 정의하는데 사용된다.
     클래스에 부여하면 해당 클래스는 다른 클래스에서 상속받을 수 없게 된다.
     메소드에 부여하면 해당 메소드를 오버라이딩 할 수 없게 된다.

    2. static
     메소드, 필드, 초기화 블록(initializer block)에 부여 가능한 제어자이다.
     이 제어자가 부여된 속성은 클래스 속성으로 정의가 된다. 다시 말해, 인스턴스를 생성하지 않고 클래스에서 바로 사용할 수 있게 된다.
     이는 프로그램 시작시에 단 한 번만 초기화되기 때문인데, 이후 해당 클래스의 모든 인스턴스가 공유하게 된다.

    3. abstract
     클래스, 메소드에 부여 가능한 제어자이다.
     선언부만 존재하고 구현부가 없는 메소드의 경우 '추상 메소드(abstract method)'라고 하며, 반드시 abstract 제어자를 부여해야 한다.
     또한 클래스 내부에 하나 이상의 추상 메소드가 포함될 경우, 해당 클래스도 반드시 abstract 제어자를 부여해야 한다.


    제어자를 선언할 수 있는 조합을 정리해보자면 다음과 같다.
    class              : public, (default), final, abstract
    method             : [All access modifiers], final, static, abstract
    field              : [All access modifiers], final, static
    local variable     : final
    initializer block  : static

    또한 이중 그 특성으로 인해 같이 사용하지 못하는 조합이 몇몇 존재한다.
    1. 클래스에서 (final, abstract)
    2. 메소드에서 (static, abstract), (private, abstract), (private, final 이건 가능하긴 한데 굳이 쓸 필요가 없다) 

    */
}
