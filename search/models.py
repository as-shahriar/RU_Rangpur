from django.db import models


class Report(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=60)
    session = models.CharField(max_length=60, null=True)
    dept = models.CharField(max_length=100, null=True)
    report = models.CharField(max_length=500)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Committee(models.Model):
    active = models.BooleanField(default=False)
    year = models.CharField(max_length=5)
    president = models.CharField(max_length=40)
    ast_president = models.CharField(max_length=40)

    def __str__(self):
        return self.year


class ResetCode(models.Model):
    username = models.CharField(max_length=50)
    code = models.CharField(max_length=60)

    def __str__(self):
        return self.username
