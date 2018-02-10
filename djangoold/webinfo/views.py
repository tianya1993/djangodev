from django.shortcuts import render
from django.http import HttpResponse
from  webinfo  import models
# Create your views here.
import  datetime
time=datetime.datetime.now()
def index(request):
	
	return render(request,"login.html")
def  homeinfo(request):
    
	return render(request,"homeinfo.html",{"times":time})

#user_listinfo=[]	
def userinfo(req):
	if req.method == "POST":
		user_name = req.POST.get("username",None)
		user_sex = req.POST.get("sex",None)
		user_email =  req.POST.get("email",None)
		#print(user_name,user_sex,user_email)
		#user = {"username":user_name,"sex":user_sex,"email":user_email}
		#user_list.append(user)
		#print(user_list)
	
        #将数据插入到数据库中
		models.Userinfo.objects.create(
			username=user_name,
			sex=user_sex,
			email=user_email,

		)
	user_listinfo=models.Userinfo.objects.all()
	
	return render(req,"index.html",{"user_lists":user_listinfo})