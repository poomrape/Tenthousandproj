function goto_loginpage(){
    window.location.href = "หน้า login.html";
}

// ...เมื่อกดปุ่ม NEXT
function check_value(){
    var username= document.getElementById("Usernamebox").value;
    var password= document.getElementById("Passwordbox").value;
    alert('username='+username+' password='+password);
    window.location.href = "Homepage2.html"
}