# Generated by Django 2.2 on 2019-08-30 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ru', '0013_auto_20190830_0537'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='img',
            field=models.ImageField(blank=True, default='default.png', upload_to='profile_pics'),
        ),
    ]
