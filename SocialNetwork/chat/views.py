from django.shortcuts import render
from authorization.models import User
from django.http import HttpResponse
from .models import Message, Notice
from django.shortcuts import redirect

def chat(request, id ):
    # return HttpResponse(id)
    user = User.objects.filter(id=id)
    return render(request, 'user/chat.html', {'user': user[0]})


def sendmessage(request, id):
    recipient = User.objects.filter(id=id)
    sender = User.objects.filter(username=request.COOKIES.get('user_name'), password=request.COOKIES.get('pwd'))
    message = Message()
    message.sender_id = sender[0].id
    message.recepient_id = recipient[0].id
    message.text = request.POST['text']
    message.sender = message.identify_sender()
    message.save()
    notice = Notice()
    notice.message_id = message.id
    notice.owner = id
    notice.save()
    return redirect('http://192.168.1.104:8080/chat/'+str(id)+'/')
