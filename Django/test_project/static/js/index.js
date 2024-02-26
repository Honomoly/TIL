window.onload = function() {
    let btn = document.getElementById("btn");
    btn.addEventListener('click', show_message);
};

function show_message() {
    alert("메세지 출력")
};