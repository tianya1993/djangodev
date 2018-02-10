from django.db import models

# Create your models here.
class Userinfo(models.Model):
	username =models.CharField('姓名',max_length=100)
	sex =models.CharField('性别',max_length=100)
	email =models.CharField('邮箱',max_length=100)
	
	def __str__(self):  # 在Python3中用 __str__ 代替 __unicode__
		return self.username