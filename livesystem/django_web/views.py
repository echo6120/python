# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django_web import models
from django.shortcuts import render_to_response, redirect
from django.template import Context
from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponse
from django.core.paginator import Paginator
# Create your views here.
#显示主页
def homeview(request):
    return render(request, 'home.html')

#显示插入bug页面函数
def insertbugview(request):
    return render(request, 'insertbug.html')
def insertnotifyview(request):
    return render(request, 'insertnotify.html')

#定义插入bug的函数
@csrf_protect
def insert(request):
    if request.method == "POST":
        testername = request.POST.get("testername")
        testtime= request.POST.get("testtime")
        system = request.POST.get("system")
        devicename = request.POST.get("devicename")
        bug = request.POST.get("bug")
        img = request.POST.get("img")
        isbug = request.POST.getlist("isBug")
        models.Bug.objects.create(testername=testername,testtime=testtime,system=system,devicename=devicename, bug=bug, img=img,isbug=isbug)
        bugs = models.Bug.objects.all()
        #models.Bug.save()
        return render(request,"buglist.html",{"bug_list":bugs})

#定义插入公告的函数
@csrf_protect
def insertnotify(request):
    if request.method =="POST":
        starttime = request.POST.get("starttime")
        endtime = request.POST.get("endtime")
        appversion = request.POST.get("appversion")
        downloadurl = request.POST.get("downloadurl")
        others = request.POST.get("others")
        models.Notify.objects.create(starttime=starttime, endtime=endtime, appversion=appversion, downloadurl=downloadurl, others=others,)
        notifies = models.Notify.objects.all()
        return render(request, "announce.html", {"notify_list": notifies})


#定义展示bug的函数
def list(request):
    limit =5
    bug_info = models.Bug.objects.all()
    paginator =Paginator(bug_info,limit)
    page = request.GET.get('page',1)
    loaded = paginator.page(page)

    #bug_list = models.Bug.objects.all()
    bug_list = loaded
    return render_to_response("buglist.html", {"bug_list": bug_list})

#定义展示公告的函数
def notifylist(request):
    #notify_list = models.Notify.objects.all().order_by("id")
    notify_list = models.Notify.objects.order_by("-id")
    return render_to_response("home.html", {"notify_list": notify_list})

#定义删除bug
def del_bug(request):
    id = request.GET.get('id')
    models.Bug.objects.filter(id=id).delete()
    return redirect('/buglist')

#定义删除announce
def del_notify(request):
    id = request.GET.get('id')
    models.Notify.objects.filter(id=id).delete()
    return redirect('/announce')

#修改bug
def bug_update(request):
    if request.method == 'GET':
        nid=request.GET.get('id')
        obj = models.Bug.objects.filter(id=nid).first()
        return render(request,"edit_bug.html",{'obj':obj})
    elif request.method == 'POST':
        nid = request.GET.get('nid')
        testername = request.POST.get("testername")
        testtime = request.POST.get("testtime")
        system = request.POST.get("system")
        devicename = request.POST.get("devicename")
        bug = request.POST.get("bug")
        img = request.POST.get("img")
        isbug = request.POST.getlist("isBug")
        models.Bug.objects.filter(id=nid).update(testername=testername,testtime=testtime,system=system,devicename=devicename, bug=bug, img=img,isbug=isbug)
        bugs = models.Bug.objects.all()
        #return render_to_response("edit_bug.html", {"edit_bug": bugs})
        return redirect('/buglist')