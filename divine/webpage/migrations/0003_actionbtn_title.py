# Generated by Django 2.0.6 on 2018-08-02 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpage', '0002_delete_homepage'),
    ]

    operations = [
        migrations.AddField(
            model_name='actionbtn',
            name='title',
            field=models.CharField(default='', max_length=100),
        ),
    ]
