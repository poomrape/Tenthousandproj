function goto_loginpage (){
    window.location.href = "users/login";
}

function goto_userinfomationpage (){
    window.location.href = "users/list";
}

function goto_logoutpage (){
    window.location.href = "users/logout"
}
function goto_maps(){
    window.location.href = "/maps"
}

function toggleDropdown() {
    var dropdown = document.getElementById("myDropdown");
    if (dropdown.style.display === "block") {
        dropdown.style.display = "none";
    } else {
        dropdown.style.display = "block";
    }
}


window.onclick = function(event) {
    if (!event.target.matches('.dropbtn')) {
        var dropdowns = document.getElementsByClassName("dropdown-content");
        var i;
        for (i = 0; i < dropdowns.length; i++) {
            var openDropdown = dropdowns[i];
            if (openDropdown.style.display === "block") {
                openDropdown.style.display = "none";
            }
        }
    }
}
