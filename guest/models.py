from django.db import models


# Create your models here.

class Event(models.Model):
    name = models.CharField(max_length=100)  # ����
    status = models.BooleanField()   # ״̬
    limit = models.IntegerField()    # ����
    start_time = models.DateTimeField()  # ʱ��
    address = models.CharField(max_length=500)  # ��ַ
    create_time = models.DateTimeField(auto_now=True)  # ����ʱ�䣨�Զ����ɣ�

    def __str__(self):
        return self.name


class Guest(models.Model):
    event = models.ForeignKey(Event)           # ����������id
    realname = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.IntegerField()
    type = models.CharField(max_length=10)
    sign = models.BooleanField()
    create_time = models.DateTimeField(auto_now=True)  # ����ʱ��

    def __str__(self):
        return self.realname
