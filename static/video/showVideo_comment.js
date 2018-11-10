

function insertComment(div,html){
	div.innerHTML = html + div.innerHTML;
}

function htmlComment(id,content,photo_url,firstname,lastname,likes){
	return commentHTML = `
	 <div class="new_comment" id="commentId=${id}">

										<!-- build comment -->
									 	<ul class="user_comment">

									 		<!-- current #{user} avatar --> 
										 	<!-- start user replies -->
									 	<li>
									 		
									 		<!-- current #{user} avatar -->
										 	<div class="user_avatar">
										 		<img src="${photo_url}">
										 	</div><!-- the comment body --><div class="comment_body">
										 		<p><div class="replied_to">${content}</p>
										 	</div>

										 	<!-- comments toolbar -->
										 	<div class="comment_toolbar">

										 		<!-- inc. date and time -->
										 		<div class="comment_details">
										 			<ul>
										 				<li><i class="fa fa-clock-o"></i> TO:DO</li>
										 				<li><i class="fa fa-calendar"></i>${firstname} ${lastname}</li>
										 				<li><i class="fa fa-pencil"></i> <span class="user">{{co}}</span></li>
										 			</ul>
										 		</div><!-- inc. share/reply and love --><div class="comment_tools">
										 			<ul>
										 				<li><i class="fa fa-share-alt"></i></li>
										 				<li><i class="fa fa-reply"></i></li>
										 				<li><i class="fa fa-heart love"><span class="love_amt"> ${likes}</span></i></li>
										 			</ul>
										 		</div>

										 	</div>


									 	</li>
	`
}