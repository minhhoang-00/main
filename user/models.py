from django.db import models

# Create your models here.

class user(models.Model):
    email = models.EmailField(primary_key=True)
    matkhau = models.CharField(max_length=20, blank=True)
    hoten = models.CharField(max_length=255, blank=True)
    gioitinh = models.IntegerField(default=0, blank=True)
    quequan = models.CharField(max_length=20, blank=True)
    dienthoai = models.IntegerField(default=0, blank=True)
    luotdatcho = models.IntegerField(default=0, blank=True)
    luothuy = models.IntegerField(default=0, blank=True)
    thongbao = models.CharField(max_length=255, blank=True)
    bienso = models.CharField(max_length=20, blank=True)
    loaixe = models.IntegerField(default=0, blank=True)
