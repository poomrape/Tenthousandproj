function goto_loginpage(){
    window.location.href = "Loginpage.html";
}
function get_value(){
    var username= document.getElementById("Usernamebox").value;
    var password= document.getElementById("Passwordbox").value;
    alert('username='+username+' password='+password)
    window.location.href = "Loginpage.html";
}