from copy import deepcopy
from datetime import datetime
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from mardikor.models import Register,Category,Advertisement,Employer
from django.db.models import Q
from itertools import chain
def home(request):
    categories=Category.objects.all()
    data=Advertisement.objects.filter(permission='Ha').order_by('-id')[:3]
    context={
        'data':data,
        'categories':categories
    }
    return render(request,'index.html',context)

def signup(request):
    if request.method=='POST':
        fname=request.POST['fname']
        lname=request.POST['lname']
        phone=request.POST['username']
        password=request.POST['password']
        gender=request.POST['gender']
        usr=User.objects.create_user(username=phone,password=password)
        usr.first_name=fname
        usr.last_name=lname
        usr.save()
        data=Register(user=usr,phone=phone,gender=gender)
        data.save()
        return  render(request,'signUp.html',{'status':f'{usr.first_name} muvaffaqiyatli ro`yxatdan o`tdingiz'})
    return render(request,'signUp.html')

def check_user(request):
    if request.method=='GET':
        un=request.GET['usern']
        check=User.objects.filter(username=un)
        if len(check)==1:
            return HttpResponse('Exists')
        else:
            return HttpResponse('Not Exists')
    return HttpResponse('Called')

def user_login(request):
    if request.method == 'POST':
        un = request.POST['email']
        pwd = request.POST['password']

        user = authenticate(username=un, password=pwd)
        if user:
            login(request, user)
            if user.is_superuser:
                return HttpResponseRedirect('/admin')
            else:
                res = HttpResponseRedirect('/')
                if 'rememberme' in request.POST:
                    res.set_cookie('user__id', user.id)
                    res.set_cookie('date_login', datetime.datetime.now())
                return res

        else:
            return render(request, 'login.html', {'status': 'Foydaluvchi nomi yoki paroli xato'})

    return render(request,'login.html')

@login_required
def user_logout(request):
    logout(request)
    res = HttpResponseRedirect('/')
    res.delete_cookie('user_id')
    res.delete_cookie('date_login')
    return res

@login_required
def ishBeruvchiProfile(request):
    return render(request,'ishBeruvchi.html')
@login_required
def viewProfile(request):
    return render(request,'viewProfile.html')
@login_required
def change_password(request):
    return render(request,'change_password.html')

@login_required
def change_password(request):
    context = {}
    ch = Register.objects.filter(user__id=request.user.id)
    if len(ch) > 0:
        data = Register.objects.get(user__id=request.user.id)
        context = {'data': data}
    if request.method == 'POST':
        current = request.POST['cpwd']
        newpass = request.POST['npwd']

        user = User.objects.get(id=request.user.id)
        un = user.username
        check = user.check_password(current)
        if check == True:
            user.set_password(newpass)
            user.save()
            context['msz'] = 'Parol muvaffaqiyatli yangilandi!!!'
            context['col'] = 'alert alert-success'
            user = User.objects.get(username=un)
            login(request, user)
        else:
            context['msz'] = 'Amaldagi Parol Xato'
            context['col'] = 'alert alert-danger'
    return render(request, 'change_password.html', context)

@login_required
def advertisement(request):
    context={}
    category=Category.objects.all()
    context={
        'data':category
    }
    if request.method=='POST':
        cat=request.POST['field']
        title=request.POST['title']
        text=request.POST['text']
        phone=request.POST['phone']
        address=request.POST['address']
        category=Category.objects.filter(id=cat).first()
        data=Advertisement(user=request.user,category=category,title=title,body=text,phone=phone,address=address)
        data.save()
        context['status']='Muvaffaqiyatli e`lon berdingiz !!!'
    return render(request,'advertisement.html',context)


def update_announce(request):
    context={}
    category = Category.objects.all()
    context = {
        'cats': category
    }
    if 'announceId' in request.GET:
        annId=request.GET['announceId']
        data=Advertisement.objects.get(id=annId)
        context['data']=data

        if request.method=='POST':
            catId=request.POST['cats']
            title=request.POST['title']
            body=request.POST['body']
            address=request.POST['address']
            phone=request.POST['phone']
            condition=request.POST['condition']

            cat_obj=Category.objects.get(id=catId)
            data.category=cat_obj
            data.title=title
            data.body=body
            data.address=address
            data.phone=phone
            data.condition=condition
            data.save()
            context['status']="muvaffaqiyatli o`zgatirildi"
    return render(request,'update_announce.html',context)
def myAnnouncement(request):
    context={}
    data=Advertisement.objects.filter(user__id=request.user.id)
    context['data']=data
    return render(request,'myAnnouncement.html',context)

def announce_details(request,pk):
    data=Advertisement.objects.get(id=pk)
    context={
        'info':data
    }
    return render(request,'announce_details.html',context)

def allAnounce(request):
    context={}
    data=Advertisement.objects.filter(permission='Ha')
    context['data']=data
    if 'catId' in request.GET:
        cat=request.GET['catId']
        advertise=Advertisement.objects.filter(category__id=cat)
        context['data']=advertise
    return render(request,'allAnnouncement.html',context)

def about(request):
    return render(request,'about.html')

@login_required
def employer(request):
    context={}
    isExist=Employer.objects.filter(id=request.user.id).first()
    print(isExist)
    category=Category.objects.all()
    context={
        'data':category,
        'employer':isExist
    }
    if request.method=='POST':
        cat=request.POST['field']
        age=request.POST['age']
        job=request.POST['job']
        about=request.POST['about']
        experience=request.POST['experience']
        salary=request.POST['salary']
        phone=request.POST['phone']
        address=request.POST['address']
        category=Category.objects.filter(id=cat).first()
        data=Employer(user=request.user,category=category,age=age,title=job,about=about,experience=experience,salary=salary,phone=phone,address=address)
        data.save()
        context['status']='Muvaffaqiyatli saqlandi!'
    return render(request,'employer.html',context)

def allEmployers(request):
    data=Employer.objects.filter()
    context={
        'data':data
    }
    return render(request,'allEmployers.html',context)

def employer_details(request,pk):
    data=Employer.objects.get(id=pk)
    context={
        'info':data
    }
    return render(request,'employer_details.html',context)
def update_resume(request):
    context={}
    category = Category.objects.all()
    context = {
        'cats': category
    }
    if 'resumeId' in request.GET:
        resumeId=request.GET['resumeId']
        data=Employer.objects.get(id=resumeId)
        context['data']=data

        if request.method=='POST':
            catId=request.POST['cats']
            age=request.POST['age']
            title=request.POST['job']
            about=request.POST['about']
            experience=request.POST['experience']
            salary=request.POST['salary']
            address=request.POST['address']
            phone=request.POST['phone']

            cat_obj=Category.objects.get(id=catId)
            data.category=cat_obj
            data.age=age
            data.title=title
            data.about=about
            data.about=about
            data.experience=experience
            data.salary=salary
            data.address=address
            data.phone=phone
            data.save()
            context['status']="muvaffaqiyatli o`zgatirildi"
    return render(request,'update_resume.html',context)

def search(request):
    context={}
    if request.method=='POST':
        qry=request.POST['query']
        advertise = Advertisement.objects.filter(Q(body__icontains=qry) | Q(category__name__icontains=qry))
        employer = Employer.objects.filter(Q(title__icontains=qry) | Q(category__name__icontains=qry))
        results = chain(advertise, employer)
        context['data'] = results
        res=list(deepcopy(results))
        context['res'] = res
    return render(request,'search.html',context)