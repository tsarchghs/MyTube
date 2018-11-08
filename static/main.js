
window.onload = function(e){
	console.log(e);
	authenticated_value = document.getElementById("authenticated").value;
	logout_div = document.getElementById("logout_div");
	signUp_signOut_div = document.getElementById("signUp_signOut_div");
	login_button = document.getElementById("login_button");
	login_form = document.getElementById("login_form");
	login_button.onclick = login;
	document.getElementById("logout_button").style.cssText = document.defaultView.getComputedStyle(login_button, "").cssText;
	if (authenticated_value == "True"){
		logout_div.innerHTML = "";
	} else {
		signUp_signOut_div.innerHTML = "";
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
