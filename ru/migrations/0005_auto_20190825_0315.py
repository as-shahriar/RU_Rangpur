# Generated by Django 2.2 on 2019-08-24 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ru', '0004_auto_20190825_0226'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='bio',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='blood',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='college',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='dept',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='father',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='fb',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='img',
            field=models.ImageField(blank=True, default='default.png', upload_to='profile_pics'),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='mother',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='permanent_address',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='present_address',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='school',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='session',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
