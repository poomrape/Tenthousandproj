function goto_loginpage (){
    window.location.href = "หน้า login.html";
}
function get_value(){
    var username= document.getElementById("input1").value;
    var password= document.getElementById("input2").value;
    alert('username='+username+' password='+password)
    window.location.href = "หน้า login.html";
}