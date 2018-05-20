from django.shortcuts import render
from django.http import HttpResponse
from .models import BlogPost

# Create your views here.
def blog(request):
	posts= BlogPost.objects.all().order_by('date')
	return render(request, 'blog/blog.html',{'posts': posts})

def blog_detail(request,slug):
	return HttpResponse(slug)