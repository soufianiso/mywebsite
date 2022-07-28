from django.shortcuts import render
from django.template import loader
from .models import Student
from django.http import HttpResponse
from django.template.loader import get_template
from django.contrib.auth.decorators import login_required
# Create your views here.

def mainpage(request):
	
	return render(request,'mainpage.html')






def search(request):

		
		query = request.GET.get('q')

		print(query)



		if query is not int and Student.objects.filter(first_name = query).exists():

			obj = Student.objects.get(first_name = query)

			context = {

				"content": obj.content
			}

			

			return render(request,'search.html', context = context)

		
		return HttpResponse("<h4>sorry we didn't find the student you want</h4>")



@login_required

def index(request):



		all_objects = Student.objects.all()

		print("hello")

		context = {

			'objects' : all_objects
		

		}

		return render(request, 'index.html', context = context )
	


def index_details(request, id = None):

	
	

	if Student.objects.filter(id = id ).exists():

		
		obj = Student.objects.get(id = id)

		context = {

			'name' : obj.first_name,
			'content' : obj.content			

		}


		return render(request, 'details.html', context = context)


	else:

		return HttpResponse("<h1> sorry we couldn't affor you a details of this sudent")







