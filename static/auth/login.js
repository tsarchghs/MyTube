
function login(){
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
		if (json.valid_credentials){
			console.log("Valid");
		} else {
			console.log("invalid");
		}
	})
	return false;
}

window.onload = function(e){
	console.log(e);
	login_button = document.getElementById("login_button");
	login_form = document.getElementById("login_form");
	login_button.onclick = login;
}

window.addEventListener("keyup",(event) => {
	if (event.key == "Enter"){
		if (document.activeElement == document.getElementById("login_username") ||
		   (document.activeElement == document.getElementById("login_password"))){
		   		login();
		   }
		   
	}
})
