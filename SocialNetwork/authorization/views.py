from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import User
from chat.models import *

def strtolist(string):
    massiv = []
    for i in string:
        if i == '[' or i == ']' or i == ',' or i == ' ' or i == '\'' or i == '"':
            pass
        else:
            massiv.append(int(i))
    return massiv

def login(request):
    print('test')
    if request.COOKIES.get('logged') == 'True':
        print('test23')
        return redirect('http://192.168.1.104:8080/feed')
    print('test3')
    return render(request, 'authorization/login.html', {'error_login': False})

def feed(request):
    try:
        if request.COOKIES.get('logged') == 'True':
            user = User.objects.filter(username=request.COOKIES.get('user_name'), password=request.COOKIES.get('pwd'))
            notices = Notice.objects.filter(owner=user[0].id)
            if len(notices) == user[0].notices:
                return render(request, 'authorization/feed.html', {'user': user[0], 'notices': True})
            else:
                return render(request, 'authorization/feed.html', {'user': user[0], 'notices': False, 'len': len(notices) - user[0].notices})
        else:
            # redirect('http://192.168.1.104:8080/test/login')
            user = User.objects.filter(username=request.POST['user_name'], password=request.POST['pwd'])
            if user:
                pass
            else:
                return redirect('http://192.168.1.104:8080/authorization/login')
            response = HttpResponse(render(request, 'authorization/feed.html', {'user': user[0]}))
            response.set_cookie('logged', 'True')
            response.set_cookie('user_name', user[0].username)
            response.set_cookie('pwd', user[0].password)
            return response
    except Exception as error:
        print(error)
        return redirect('http://192.168.1.104:8080/authorization/login')

def registration(request):
    try:
        user = User()
        user.name = request.POST['name']
        user.surname = request.POST['surname']
        user.username = request.POST['username']
        user.password = request.POST['pwd']
        user.age = request.POST['age']
        user.mail = request.POST['mail']
        user.friends = '[]'
        user.save()
        return redirect('http://192.168.1.104:8080/authorization/login')
    except Exception as e:
        return render(request, 'authorization/registration.html')

def list(request):
    if request.COOKIES.get('logged') == 'True':
        users = User.objects.filter(username=request.COOKIES.get('user_name'), password=request.COOKIES.get('pwd'))
        user = users[0]
        users = User.objects.all()
        massiv = []
        for i in range(len(users)):
            if users[i].id == user.id:
                pass
            else:
                massiv.append(users[i])
        return render(request, 'authorization/list_users.html', {'users': massiv})
    else:
        return redirect('http://192.168.1.104:8080/test/login')

def user_detail(request, user_id):
    users = User.objects.filter(id=user_id)
    userss = User.objects.filter(username=request.COOKIES.get('user_name'), password=request.COOKIES.get('pwd'))
    if len(users) == 0:
        return HttpResponse('User not fount')
    else:
        user = userss[0]
        user.friends = strtolist(user.friends)
        print(user.friends)
        # try:
        #     if user_id in user.friends:
        #         isfriend = False
        # except Exception as e:
        #     isfriend = True
        if not len(user.friends) == 0:
            if user_id in user.friends:
                isfriend = False
        else: isfriend = True
        return render(request, 'authorization/user_detail.html', {'user': users[0], 'isfriend': isfriend})
