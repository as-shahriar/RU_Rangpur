# Generated by Django 2.2 on 2019-08-24 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ru', '0003_auto_20190825_0217'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userinfo',
            name='bio',
        ),
        migrations.RemoveField(
            model_name='userinfo',
            name='blood',
        ),
        migrations.RemoveField(
            model_name='userinfo',
            name='college',
        ),
        migrations.RemoveField(
            model_name='userinfo',
            name='dept',
        ),
        migrations.RemoveField(
            model_name='userinfo',
            name='father',
        ),
        migrations.RemoveField(
            model_name='userinfo',
            name='fb',
        ),
        migrations.RemoveField(
            model_name='userinfo',
            name='img',
        ),
        migrations.RemoveField(
            model_name='userinfo',
            name='mother',
        ),
        migrations.RemoveField(
            model_name='userinfo',
            name='permanent_address',
        ),
        migrations.RemoveField(
            model_name='userinfo',
            name='present_address',
        ),
        migrations.RemoveField(
            model_name='userinfo',
            name='school',
        ),
        migrations.RemoveField(
            model_name='userinfo',
            name='session',
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
