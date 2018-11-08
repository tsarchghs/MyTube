
/*
<div class="alert alert-danger">
									  Username or Password was wrong, please try again.
								</div>
								*/
function login(){
	var login_alert = document.getElementById("login_alert");
	var csrftoken = Cookies.get('csrftoken');
	var username = document.getElementById("login_username").value;
	var password = document.getElementById("login_password").value;
	return fetch('http://localhost:8000/api/validate_credentials/?format=json', {
		method: "POST",
		headers: {
		    'Accept': 'application/json, text/plain, */*',
		    'Content-Type': 'application/json',
		    "X-CSRFToken":csrftoken
		  },		
		body: JSON.stringify({"username":username,"password":password})
	})
	.then(function(response){
		return response.json();
	})
	.then(function(json){
		var formData = new FormData();
		formData.append("username",username);
		formData.append("password",password);
		if (json.valid_credentials){
			fetch('http://localhost:8000/auth/login', {
				method: "POST",	
				headers: {
					"X-CSRFToken":csrftoken
				},
				body: formData
			})
			login_alert.innerHTML = "";

		} else {
			var div = document.createElement("div");
			div.className = "alert alert-danger";
			div.innerHTML = "<h6>Username or Password was wrong, please try again.</h6>";
			login_alert.appendChild(div);
		}
	})
}

window.onload = function(e){
	console.log(e);
	login_button = document.getElementById("login_button");
	login_form = document.getElementById("login_form");
	login_button.onclick = login;
	document.getElementById("logout_button").style.cssText = document.defaultView.getComputedStyle(login_button, "").cssText;

}

window.addEventListener("keyup",(event) => {
	if (event.key == "Enter"){
		if (document.activeElement == document.getElementById("login_username") ||
		   (document.activeElement == document.getElementById("login_password"))){
		   		login();
		   }
		   
	}
})
