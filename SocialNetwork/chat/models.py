from django.db import models
from authorization.models import User
# Create your models here.


class Notice(models.Model):
    message_id = models.IntegerField()
    owner = models.IntegerField()


def identify_sender(sender_id):
    sender = User.objects.get(id=sender_id)
    return sender.name

class Message(models.Model):
    text = models.TextField()
    sender_id = models.IntegerField()
    recepient_id = models.IntegerField()
    sender = models.CharField(max_length=50)

    def identify_sender(self):
        sender = User.objects.get(id=self.sender_id)
        return sender.name

    def identify_recepient(self):
        recepient = User.objects.get(id=self.recepient_id)
        return recepient.name
