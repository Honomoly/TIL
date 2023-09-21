window.onload=function(){
    document.getElementById("newform").onsubmit=function(e){
let chk= false;
let chk1= false;
let chk2= false;
for(i=0; i<2; i++){
    if(newform.usefor[i].checked==true){chk=true;}
        if(newform.personal[i].checked==true){chk1=true;}
        if(newform.year[i].checked==true){chk2=true;}
       
       }

    if(chk==false||chk1==false||chk2==false){
        alert("모두 체크해주세요");
        return false;
        }
       
    k=document.querySelector('input[name="usefor"]:checked').value;
    if(k=='2'){alert('모두 동의하세요')
    return false;}
    
    s=document.querySelector('input[name="personal"]:checked').value;
    if(s=='2'){alert('모두 동의하세요')
    return false;}

    age=document.querySelector('input[name="year"]:checked').value;
    
    if(age=='2'){
        alert('회원가입 페이지로 넘어갑니다.')
        e.preventDefault()
        location.href="join.html"  
        
    }else { alert('회원가입 페이지로 넘어갑니다.')
        e.preventDefault()
        location.href="join_young.html"
        
    }

    }
    



}