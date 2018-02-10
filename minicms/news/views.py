
from django.shortcuts import render
from django.http import HttpResponse
from  news import  models
 
def index(request):
    return HttpResponse(u'欢迎来自强学堂学习Django')
 
 
def column_detail(request, column_slug):
    return HttpResponse('column slug: ' + column_slug)
 
 
def article_detail(request, article_slug):
    return HttpResponse('article slug: ' + article_slug)
def  articleinfo(req):
	userlist=models.Article.objects.all()
	return render(req,"index.html",{"user_info":userlist})

