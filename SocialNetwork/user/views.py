from django.shortcuts import render
from authorization.models import User
from chat.models import Notice, Message
from django.http import HttpResponse
def add_friend(request, user_id):
    def strtolist(string):
        massiv = []
        for i in string:
            if i == '[' or i == ']' or i == ',' or i == ' ' or i == '\'' or i == '"':
                pass
            else:
                massiv.append(int(i))
        return massiv
    users = User.objects.filter(username=request.COOKIES.get('user_name'), password=request.COOKIES.get('pwd'))
    user = users[0]
    user.friends = strtolist(user.friends)
    user.friends.append(int(user_id))
    user.friends = str(user.friends)
    user.save()
    user = User.objects.get(id=user_id)
    return render(request, 'user/added.html', {'user': user})

def notices(request, id):
    user = User.objects.get(id=id)
    notices = Notice.objects.filter(owner=user.id)
    user.notices = len(notices)
    user.save()
    messages = Message.objects.filter(recepient_id=user.id)
    for i in messages:
        print(i.sender)
    return render(request, 'user/notices.html', {'messages': messages})

def notice(request, message_id):
    message = Message.objects.get(id=message_id)
    return render(request, 'user/notice.html', {'message': message})

def friends(request, id):
    def strtolist(string):
        massiv = []
        for i in string:
            if i == '[' or i == ']' or i == ',' or i == ' ' or i == '\'' or i == '"':
                pass
            else:
                massiv.append(int(i))
        return massiv
    user = User.objects.get(id=id)
    friends = strtolist(user.friends)
    print(friends)
    data = []
    for i in friends:
        data.append(User.objects.get(id=i))
    for i in data:
        print(i.name)
    return render(request, 'user/friends.html', {'friends':data})