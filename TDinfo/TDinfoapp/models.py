from django.db import models

# Create your models here.
class TDinfo(models.Model):
 
    title = models.CharField('标题', max_length=256)
    slug = models.CharField('网址', max_length=256, db_index=True)
    author = models.ForeignKey('auth.User', blank=True, null=True, verbose_name='作者',on_delete='作者')
    content = models.CharField('内容', max_length=256)
    published = models.BooleanField('正式发布', default=True)
    pub_date = models.DateTimeField('发表时间', auto_now_add=True, editable=True)
    update_time = models.DateTimeField('更新时间', auto_now=True, null=True)
 
    def __str__(self):
        return self.title