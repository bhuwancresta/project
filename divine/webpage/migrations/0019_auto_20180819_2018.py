# Generated by Django 2.1 on 2018-08-19 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpage', '0018_auto_20180816_2052'),
    ]

    operations = [
        migrations.DeleteModel(
            name='AuthorName',
        ),
        migrations.DeleteModel(
            name='HouseDimenssion',
        ),
        migrations.RemoveField(
            model_name='innerfeature',
            name='about_project',
        ),
        migrations.RemoveField(
            model_name='innerfeature',
            name='slide_image',
        ),
        migrations.AddField(
            model_name='innerfeature',
            name='about',
            field=models.TextField(default='', max_length=400),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='innerfeature',
            name='author1',
            field=models.CharField(default='', max_length=60),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='innerfeature',
            name='author2',
            field=models.CharField(default='', max_length=60),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='innerfeature',
            name='position1',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='innerfeature',
            name='position2',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='innerfeature',
            name='slide_image1',
            field=models.ImageField(default='', upload_to=''),
        ),
        migrations.AddField(
            model_name='innerfeature',
            name='slide_image2',
            field=models.ImageField(default='', upload_to=''),
        ),
        migrations.AddField(
            model_name='innerfeature',
            name='slide_image3',
            field=models.ImageField(default='', upload_to=''),
        ),
    ]
