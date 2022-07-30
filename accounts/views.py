from django.shortcuts import render , redirect
from django.contrib.auth import authenticate, login, logout

from django.http import HttpResponse

from .forms import ArticleForm

# Create your views here.



def login_view(request):


	
	form = ArticleForm()


	
	context = { 

			'form' : form

		}




	if request.method == "POST":

		username = request.POST.get('username')
		password = request.POST.get('password')



		user = authenticate(request, username = username, password = password)

		if user is None:

			context = {

				"error": "invalid password or username"

			} 

			return render(request,"accounts/login.html", context = context) 

		
		
		login(request,user)

		return redirect('/index')

		
	return render(request,"accounts/login.html")


def logout_view(request):

	if request.method == "POST":

		logout(request)
		return  redirect("/login")


	return render(request, "accounts/logout.html", {})


def register_view(request):

	return render(request, "", {})



hello world