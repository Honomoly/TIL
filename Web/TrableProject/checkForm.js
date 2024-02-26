// 폼 유효성 확인

window.onload=function(){
    //폼의 유효성 확인
    //폼의 회원가입 버튼 눌렀을 때: submit 이벤트발생
    document.getElementById("joinForm").onsubmit=function(e){
        //섬영을 입력하지 않은 경우 알림창 출력
        let name=document.getElementById('name');
        if(name.value==""){//성명란 공백일경우
            alert("성명을 입력하세요")
            name.focus(); //성명 입력란에 포커스
            return false; //넘어가지 못하도록

        }

        //id의 value값을 가져와서 비었는지 확인
        let id=document.getElementById('id');
        if(id.value==""){
            alert("id를 입력하세요");
            id.focus(); 
            return false;
            };
        //id 길이 확인, 입력한 값의 길이 확인.value.length
        if(id.value.length<6 ){
            alert("id를 6자 이상으로 입력하세요");
            id.value="";
            id.focus(); 
            return false;
        }
        

        //비밀번호 일치 확인
        let pw= document.getElementById('password')
        let pwcheck= document.getElementById('passwordCheck')
        if(pw.value!=pwcheck.value){
            alert("비밀번호 확인이 일치하지 않습니다.")
            pwcheck.value=""
            pwcheck.focus();
            return false;

        }

        //비밀번호 길이 확인
        if(pw.value.length<8 || pw.value.length>12 ){
            alert("비밀번호를 8자~12자로 입력하세요");
            pw.value="";
            pw.focus(); 
            return false; }
          
        
        //비밀번호 특수기호 꼭 포함 @!#$    
        let numc=0;
        let chek=0;
        let code=["!","@","#","$","%"];
        let num=[1,2,3,4,5,6,7,8,9,0]
        for(i=0; i<code.length; i++){
        if(pw.value.indexOf(code[i])!=-1   ){
            chek=-1} }
            if(chek==0){
                alert("비밀번호에 !@#$%를 포함하세요");
                pw.value="";
                pwcheck.value=""
                pw.focus(); 
                return false; } 
            
        for(i=0; i<num.length; i++){    
            if(pw.value.indexOf(num[i])!=-1   ){
                numc=-1}}

                if(numc==0){
                alert("비밀번호에 숫자를 포함하세요");
                pw.value="";
                pwcheck.value=""
                pw.focus(); 
                return false; } 
       
        //직업선택 여부 확인
        let way=document.getElementById('way')
        if(way.selectedIndex==0){
            alert("가입경로를 선택하시오")
            return false;
        
        }

        // 라디오버튼- 이메일 수신여부
        // 라디오 버튼의 경우에는 id 속성을 사용하지 않고 그룹 이름인 naem 속성 사용
        //  동일 그룹에 속한 여러 라디오 객체는 name 동일
        //그룹 내에 여러 개의 라디오 객체가 있으므로 배열(for문 사용)로 처리함
        let chk= false; //체크 여부 확인하는 변수. false로 초기화
        for(i=0; i<joinForm.emailRcv.length; i++){
            if(joinForm.emailRcv[i].checked==true){
                chk=true; //하나라도 체크되면 true로 설정
            }
        }

        //하나도 선택되지 않으면 false 값 그대로
        if(chk==false){
            alert("이메일 수신 여부를 선택하세요");
            return false;
        }

        //체크박스 checkbox=> 여러개 선택 가능
        let ch1=document.getElementById('reason1');
        let ch2=document.getElementById('reason2');
        let ch3=document.getElementById('reason3');
        let ch4=document.getElementById('reason4');
        if(ch2.checked==false && ch1.checked==false && 
            ch3.checked==false && ch4.checked==false){
        
            alert("여행 목적을 선택해주세요")
            return false
        }   
    }}