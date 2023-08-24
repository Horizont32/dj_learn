from django.db import models
from django.urls import reverse


# Create your models here.

class User(models.Model):
    user_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    nickname = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name, self.nickname}'

    def get_abs_url(self):
        return reverse('categs', kwargs={'id': self.user_id})

class Message(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.CharField(max_length=255)
    date = models.DateField(auto_now_add=True)


class Event(models.Model):
    event_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    summ = models.IntegerField()
    payer = models.ForeignKey(User, on_delete=models.CASCADE)


class Event_Ower(models.Model):
    event_id = models.ForeignKey(Event, on_delete=models.CASCADE)
    ower_id = models.ForeignKey(User, on_delete=models.CASCADE)
    owed_summ = models.IntegerField()
