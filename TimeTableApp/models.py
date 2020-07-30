from django.db import models
from django.db.models import CharField
# Create your models here.
from django.contrib.auth.models import User
from django_mysql.models import ListCharField



class Table(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    table_data = ListCharField(base_field=CharField(max_length=32, blank=True,null=True),max_length=1024)
    rows = models.CharField(max_length=10)
    col = models.CharField(max_length=10)
    name = models.CharField(max_length=132)
