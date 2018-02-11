"""minicms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
#from django.urls import path, re_path
from news  import views as news_views
from django.contrib import admin
from django.conf.urls import include, url
from django.urls import path , re_path
from DjangoUeditor import urls as DjangoUeditor_urls
urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^ueditor/', include(DjangoUeditor_urls)),
    path('',news_views.index, name='index'),
    path('dictinfo/', news_views.dictinfo,name="dictinfo"),
    re_path(r'^column/(?P<column_slug>[^/]+)/$',news_views.column_detail,name='column'),
    #re_path(r'^news/(?P<article_slug>[^/]+)/$',news_views.article_detail,name='article'),
    #re_path('column/', news_views.column_detail, name='column'),
    path('news/', news_views.article_detail, name='article'),
    path('', news_views.articleinfo, name='articleinfo '),
    re_path(r'^news/(?P<pk>\d+)/(?P<article_slug>[^/]+)/$', news_views.article_detail, name='article'),
  #  path('userinfo/',news_views.userinfo,name='usrinfo')

 
]

"""

urlpatterns = [
 	url(r'^$', 'news.views.index', name='index'),
    url(r'^column/(?P<column_slug>[^/]+)/$', 'news.views.column_detail', name='column'),
    url(r'^news/(?P<article_slug>[^/]+)/$', 'news.views.article_detail', name='article'),
    url(r'^admin/', include(admin.site.urls))
    ]
  """ 


# use Django server /media/ files
from django.conf import settings
 
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

