"""livesystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from django_web import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^home', views.notifylist),
    url(r'^buglist/', views.list),
    url(r'^announce/', views.notifylist),
    url(r'^insertbug/', views.insert),
    url(r'^insertbugview/',views.insertbugview),
    url(r'^insertnotifyview/',views.insertnotifyview),
    url(r'^insertnotify/', views.insertnotify),
    url(r'^del_bug', views.del_bug),
    url(r'^edit_bug', views.bug_update),
    url(r'^del_notify', views.del_notify),
]
