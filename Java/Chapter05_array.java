import java.util.Arrays;

public class Chapter05_array {
    public static void main(String[] args) {
        // 배열
        // 같은 타입의 변수들로 이루어진 유한 순서쌍이다. 마찬가지로 인덱스가 0에서 시작하는 방식이다.

        // 1. 1차원 배열

        // 선언법
        int[] arr1;
        // int arr1[]; // 이 방식은 별로라고 하네?

        // 선언후에 크기 할당 가능
        arr1 = new int[4]; // 내부의 숫자는 배열의 길이를 뜻한다

        // 선언과 동시에 크기 할당하기
        int[] arr2 = new int[5];

        /*
        할당이나 length 속성과 관해서는 javascript와 꽤나 흡사하다.
        다만 한 번에 값까지 초기화 하기 위해서는 주의할 점이 존재한다.
        */

        // 명시적(리터럴)으로 값 할당하기
        int[] arr3 = {2, 3, 4, 5};
        int[] arr4 = new int[]{3, 4, 5, 6}; // new로 값 할당하는 것도 된다

        // 다만 이미 선언된 배열은 new 없이는 값을 할당할 수 없다.
        // arr2 = {4, 5, 6, 7}; // 오류남
        arr2 = new int[]{4, 5, 6, 7}; // 이 방식으로만 초기화할 수 있다.

        // 배열 출력해보기
        for (int i=0; i<arr2.length; i++) {
            System.out.print(arr2[i] + " ");
        }
        // sum이나 mean같은 간단한 메소드도 없으니 그냥 알아서 수동으로 구현하자. 어차피 컴파일 언어다.

        System.out.println("\n--1--");


        // 2. 2차원 배열

        // 선언법
        int[][] arr5; // 그냥 이거 쓰자
        // int arr5[][];
        // int[] arr5[];

        // 선언 및 크기 할당
        int[][] arr6 = new int[3][4]; // 3 x 4 크기의 배열을 만든다

        // 수동 초기화
        for (int i=0; i<arr6.length; i++) {
            for (int j=0; j<arr6[i].length; j++) {
                arr6[i][j] = i*arr6[i].length + j;
            }
        }

        // 출력
        for (int i = 0; i < arr6.length; i++) {
            for (int j = 0; j < arr6[i].length; j++) {
                System.out.print(arr6[i][j] + "\t");
            }
            System.out.println();
        }

        // 1차원 배열과 비슷하게 선언과 동시에 명시적으로 값 할당이 가능하다.
        arr5 = new int[][]{
            {1, 2, 3},
            {4, 5, 6}
        }; // 보기 좋게 적당히 탭과 줄바꿈 사용

        // 가변 배열 또한 가능하다.
        int[][] arr7 = {
            {1, 2},
            {3, 4, 5},
            {6}
        };


        // 3. 배열의 복사

        /*
        자바는 배열을 한 번 생성하면 길이 변경이 불가능하기 때문에 기존 배열에서 새로운 정보의 추가를 위해서는
        더 큰 크기의 배열을 만들고 그 안에 복사하는 방법 밖에 없다.
        */

        int[] arr_src = {2, 3, 5, 7, 11, 13};

        // 가장 성능이 좋은 arraycopy() 메소드
        // 입력 순서 : 원본 배열, 원본 배열의 복사 시작 부분, 복사 배열, 복사 배열의 복사 시작 부분, 복사하는 길이
        int[] arr_copy1 = new int[10];
        System.arraycopy(arr_src, 2, arr_copy1, 4, 4);
        
        // Enhanced for문으로 출력
        System.out.println("--arraycopy--");
        for (int e: arr_copy1) {System.out.print(e + "\t");}

        // 유연함 때문에 가장 많이 쓰인다는 copyOf() 메소드
        int[] arr_copy2 = Arrays.copyOf(arr_src, 10);

        System.out.println("\n--copyOf--");
        for (int e: arr_copy2) {System.out.print(e + "\t");}
    }

}
