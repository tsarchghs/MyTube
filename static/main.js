

var comments_count = 0;


window.onload = function(e){
	console.log(e);
	authenticated_value = document.getElementById("authenticated").value;
	login_button = document.getElementById("login_button");
	login_form = document.getElementById("login_form");
	if (login_button != null){
		login_button.onclick = login;
	}
	if (document.getElementById("video_id")){
		addComments(comments_count,comments_count+5);
		comments_count += 5;
	}
	document.getElementById("like_a").onclick = () => {
		authenticated = document.getElementById("authenticated").value;
		console.log(authenticated);
		if (authenticated == "True"){
			like("like");
		} else {
			document.getElementById("signin_popup_button").click();
		}
		return false;
	}
	document.getElementById("dislike_a").onclick = () =>{
		authenticated = document.getElementById("authenticated").value;
		if (authenticated == "True"){
			like("dislike");
		} else {
			document.getElementById("signin_popup_button").click();
		}		
		return false;
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
