# Generated by Django 2.2 on 2022-06-12 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('matkhau', models.CharField(blank=True, max_length=20)),
                ('hoten', models.CharField(blank=True, max_length=255)),
                ('gioitinh', models.IntegerField(blank=True, default=0)),
                ('quequan', models.CharField(blank=True, max_length=20)),
                ('dienthoai', models.IntegerField(blank=True, default=0)),
                ('luotdatcho', models.IntegerField(blank=True, default=0)),
                ('luothuy', models.IntegerField(blank=True, default=0)),
                ('bienso', models.CharField(blank=True, max_length=20)),
                ('loaixe', models.IntegerField(blank=True, default=0)),
            ],
        ),
    ]
