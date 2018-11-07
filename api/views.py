from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate

# Create your views here.

class ValidateCredentials(APIView):
	permission_classes = []
	def get(self,request):
		content = {"post_only":True}
		return Response(content)
	def post(self,request):
		username = request.data.get("username")
		password = request.data.get("password")
		user = authenticate(username=username,password=password)
		if user is not None:
			content = {"valid_credentials":True}
		else:
			content = {"valid_credentials":False}
		return Response(content)