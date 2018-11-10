
window.onload = function(e){
	console.log(e);
	authenticated_value = document.getElementById("authenticated").value;
	login_button = document.getElementById("login_button");
	login_form = document.getElementById("login_form");
	if (login_button != null){
		login_button.onclick = login;
	}
}

window.addEventListener("keyup",(event) => {
	if (event.key == "Enter"){
		if (document.activeElement == document.getElementById("login_username") ||
		   (document.activeElement == document.getElementById("login_password"))){
		   		login();
		   }
		   
	}
})
