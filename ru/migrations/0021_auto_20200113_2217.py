# Generated by Django 2.2 on 2020-01-13 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ru', '0020_auto_20200113_2148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='bio',
            field=models.TextField(blank=True, max_length=100, null=True),
        ),
    ]
