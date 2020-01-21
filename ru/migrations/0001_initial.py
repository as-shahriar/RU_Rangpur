# Generated by Django 2.2 on 2019-08-24 15:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('mobile', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=80)),
                ('present_address', models.CharField(max_length=300)),
                ('permanent_address', models.CharField(blank=True, max_length=300)),
                ('school', models.CharField(max_length=200)),
                ('college', models.CharField(max_length=200)),
                ('dept', models.CharField(max_length=100)),
                ('session', models.CharField(max_length=20)),
                ('blood', models.CharField(max_length=5)),
                ('father', models.CharField(max_length=100)),
                ('mother', models.CharField(max_length=100)),
                ('fb', models.CharField(blank=True, max_length=100)),
                ('bio', models.CharField(blank=True, max_length=500)),
                ('img', models.ImageField(blank=True, default='default.jpg', upload_to='profile_pics')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
