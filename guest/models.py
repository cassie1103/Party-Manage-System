from django.db import models


# Create your models here.

class Event(models.Model):
    name = models.CharField(max_length=100)  # 名称
    status = models.BooleanField()   # 状态
    limit = models.IntegerField()    # 人数
    start_time = models.DateTimeField()  # 时间
    address = models.CharField(max_length=500)  # 地址
    create_time = models.DateTimeField(auto_now=True)  # 创建时间（自动生成）

    def __str__(self):
        return self.name


class Guest(models.Model):
    event = models.ForeignKey(Event)           # 关联发布会id
    realname = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.IntegerField()
    type = models.CharField(max_length=10)
    sign = models.BooleanField()
    create_time = models.DateTimeField(auto_now=True)  # 创建时间

    def __str__(self):
        return self.realname
