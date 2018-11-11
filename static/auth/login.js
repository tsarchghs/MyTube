
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
	var authenticated = document.getElementById("authenticated").value;
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
			var small_dialog = document.getElementById("small-dialog");
			fetch('http://localhost:8000/auth/login', {
				method: "POST",	
				headers: {
					"X-CSRFToken":csrftoken
				},
				body: formData
			}).then(function(response){
				fetch("http://localhost:8000/api/get_current_user_profile/?format=json",{
					method: "GET",
					headers: {
						"Accept": "application/json",
						"Content-Type":"application/json"
					}
				}).then(function(response){
					return response.json();
				}).then(function(json){
					json_ = JSON.parse(json);
					profile = json_[0];
					userProfile_info = document.getElementById("userProfile_info");
					userProfile_id = document.getElementById("userProfile_id")
					console.log(profile);
					if (userProfile_id){
						userProfile_id.value = profile.pk;
					} else {
						userProfile_id = document.createElement("input");
						userProfile_id.type = "hidden";
						userProfile_id.id = "userProfile_id";
						userProfile_id.value = profile.pk;
						console.log(profile.pk);
						userProfile_info.appendChild(userProfile_id);
					}
				})
			}).then(function(response){
				document.getElementById("authenticated").value = "True";
				login_alert.innerHTML = "";
				document.getElementById("register_div").style.display = "none";
				document.getElementById("login_div").style.display = "none";
				console.log(small_dialog);
				small_dialog.innerHTML = "";
				var div = document.createElement("div");
				div.id = "logged_in_alert";
				div.className = "alert alert-success";
				div.innerHTML = "<h6>Logged in successfully.</h6>";
				small_dialog.appendChild(div);
			})
		} else {
			if (!document.getElementById("invalid_credentials_alert")){
				var div = document.createElement("div");
				div.id = "invalid_credentials_alert";
				div.className = "alert alert-danger";
				div.innerHTML = "<h6>Username or Password was wrong, please try again.</h6>";
				login_alert.appendChild(div);
			}
		}
	})
}