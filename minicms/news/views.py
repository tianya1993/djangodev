
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

def column_detail(request, column_slug):
	column = models.Column.objects.get(slug=column_slug)
	return render(request, 'news/column.html', {'column': column})

"""
def article_detail(request, article_slug):
	article = models.Article.objects.get(slug=article_slug)
	return render(request, 'news/article.html', {'article': article})
"""
def article_detail(request, pk, article_slug):
    article = models.Article.objects.get(pk=pk)
    return render(request, 'news/article.html', {'article': article})
def index(request):
    columns = models.Column.objects.all()
    return render(request, 'hindex.html', {'columns': columns})
def dictinfo(request):
	stu_dict={"name":"中国计算机","age":"40","address":"浙江省杭州市","telphone":"18393358888"}
	return  render(request,"dict.html",{"stu_dicts":stu_dict})