# Generated by Django 2.0.6 on 2018-08-03 02:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webpage', '0005_auto_20180803_0822'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='actionbtn',
            name='image',
        ),
    ]
