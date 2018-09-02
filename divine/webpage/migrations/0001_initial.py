# Generated by Django 2.0.6 on 2018-08-02 02:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ActionBtn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='BannerImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('banner_image', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='FeatureName',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('house_name', models.CharField(max_length=150)),
                ('image', models.ImageField(upload_to='')),
                ('dimention', models.CharField(max_length=60)),
                ('beds', models.PositiveIntegerField()),
                ('bath', models.PositiveIntegerField()),
                ('width', models.CharField(max_length=60)),
                ('depth', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='HomeChoose',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('title', models.CharField(max_length=120)),
                ('describe', models.TextField(max_length=330)),
            ],
        ),
        migrations.CreateModel(
            name='HomePage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='HomeService',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('title', models.CharField(max_length=120)),
                ('describe', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('name', models.CharField(max_length=60)),
                ('company', models.CharField(max_length=60)),
                ('describe', models.TextField(max_length=250)),
            ],
        ),
    ]
