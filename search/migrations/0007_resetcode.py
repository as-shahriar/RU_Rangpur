# Generated by Django 2.2 on 2019-09-07 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0006_auto_20190903_1825'),
    ]

    operations = [
        migrations.CreateModel(
            name='ResetCode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('code', models.CharField(max_length=60)),
            ],
        ),
    ]
