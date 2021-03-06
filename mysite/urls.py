"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_view
from log.forms import LoginForm

urlpatterns = [
    url(r'^login/$', include('log.urls')),
    url(r'^logout/$', auth_view.logout, {'next_page': '/login'}, name='logout'),
	url(r'^polls/', include('polls.urls')),
    url(r'^chef/', include('chef.urls')),
    #url(r'^orders/',include('orders.urls')),
	url(r'^$', include('addfood.urls')),
    url(r'^menu/', include('menu.urls')),
    url(r'^waiter/',include('waiter.urls')),
    url(r'^admin/', admin.site.urls),
]