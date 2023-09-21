window.onload = function() {
    let birth_month = document.getElementById('birth_month');
    for (let i=1; i<=12; i++) {
        let option = document.createElement("option");
        option.value = i;
        let text = document.createTextNode(`${i}`);
        option.appendChild(text);
        birth_month.appendChild(option);
    }

    let birth_date = document.getElementById('birth_date');
    

    // 폼 유효성 확인
    // 회원가입 버튼을 눌렀을 시 처리 시작
    document.getElementById('joinForm').onsubmit = function() {
        // (1) 이름 확인
        let name = document.getElementById('name');
        if (name.value == "") {
            alert("성명을 입력하세요");
            name.focus(); // 성명 입력란 주목
            return false; // 다음 과정으로 넘어가지 못하게 한다
        }

        // (2) 아이디 확인
        let id = document.getElementById('id');
        if (id.value == "") {
            alert("아이디를 입력하세요");
            id.focus(); // 아이디 입력란 주목
            return false; // 다음 과정으로 넘어가지 못하게 한다
        } else if (id.value.length<6||id.value.length>10) {
            alert("아이디를 6~10자 이내로 입력하세요");
            id.value = "";
            id.focus();
            return false;
        }

        // (3) 비밀번호 확인
        let password = document.getElementById('password');
        let pw_check = document.getElementById('pw_check');
        if (password.value != pw_check.value) {
            alert("입력한 비밀번호가 서로 일치하지 않습니다")
            pw_check.value = "";
            pw_check.focus();
            return false;
        }

        // (4) 직업선택 확인
        let job = document.getElementById('job');
        // 방법1. selectedIndex 속성 사용
        // if (job.selectedIndex == 0) {
        //     alert("직업을 선택하세요");
        //     return false;
        // }
        // 방법2. value 속성 사용
        if (job.value == "") {
            alert("직업을 선택하세요");
            return false;
        }

        // (5) 라디오 버튼 (주의! name 속성을 사용!)
        // 체크를 하면 checked 속성이 true가 되고 그 반대또한 된다
        let emailRcv = document.getElementsByName('emailRcv');
        let checking = false; // 체크 여부를 확인하기 위한 변수
        for (let i=0; i<emailRcv.length; i++) {
            if (emailRcv[i].checked) {
                checking = true;
                break;
            }
        }
        if (!checking) {
            alert("이메일 수신여부를 확인하세요")
            return false;
        }

        // (6) 체크박스
        // joinForm 안에 있는 것으로 바로 불러올 수 있다
        let checking2 = false; // 체크 여부를 확인하기 위한 변수
        for (let i=0; i<joinForm.agreement.length; i++) {
            if (joinForm.agreement[i].checked) {
                checking2 = true;
                break;
            }
        }
        if (!checking2) {
            alert("약관 동의 여부를 확인하세요")
            return false;
        }

    };
};