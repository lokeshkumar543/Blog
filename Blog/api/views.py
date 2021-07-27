from django.shortcuts import render, HttpResponseRedirect
from .models import Blog

def listing_data(request):
    b=Blog.objects.all()
    return render(request,'index.html',{'data':b})

def add(request):
    b= Blog()
    if (request.method=='POST'):
        b.title=request.POST.get('title')
        b.description=request.POST.get('description')
        b.image=request.FILES.get('image')
        b.author_name=request.POST.get('authorname')
        b.author_email=request.POST.get('authoremail')
        b.author_phone=request.POST.get('authorphone')
        b.save()
        return HttpResponseRedirect('/')
    return render(request,'Add.html')

def delete(request,num):
    b=Blog.objects.filter(id=num)
    b.delete()
    return HttpResponseRedirect('/')


