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
    president = models.CharField(
        max_length=40, null=True, blank=True, default="N/A")
    ast_president_1 = models.CharField(
        max_length=40, null=True, blank=True, default="N/A")
    ast_president_2 = models.CharField(
        max_length=40, null=True, blank=True, default="N/A")
    ast_president_3 = models.CharField(
        max_length=40, null=True, blank=True, default="N/A")
    general_secretary = models.CharField(
        max_length=40, null=True, blank=True, default="N/A")
    ast_general_secretary_1 = models.CharField(
        max_length=40, null=True, blank=True, default="N/A")
    ast_general_secretary_2 = models.CharField(
        max_length=40, null=True, blank=True, default="N/A")
    sangothonik_sompadok = models.CharField(
        max_length=40, null=True, blank=True, default="N/A")
    treasurer = models.CharField(
        max_length=40, null=True, blank=True, default="N/A")

    ast_treasurer_1 = models.CharField(
        max_length=40, null=True, blank=True, default="N/A")
    ast_treasurer_2 = models.CharField(
        max_length=40, null=True, blank=True, default="N/A")
    doptor_sompadok = models.CharField(
        max_length=40, null=True, blank=True, default="N/A")
    prochar_sompadok = models.CharField(
        max_length=40, null=True, blank=True, default="N/A")
    appayon_sompadok = models.CharField(
        max_length=40, null=True, blank=True, default="N/A")
    sikkha_krira_sangskritik_sompadok = models.CharField(
        max_length=40, null=True, blank=True, default="N/A")
    member_1 = models.CharField(
        max_length=40, null=True, blank=True, default="N/A")
    member_2 = models.CharField(
        max_length=40, null=True, blank=True, default="N/A")
    member_3 = models.CharField(
        max_length=40, null=True, blank=True, default="N/A")
    member_4 = models.CharField(
        max_length=40, null=True, blank=True, default="N/A")

    def __str__(self):
        return self.year


class ResetCode(models.Model):
    username = models.CharField(max_length=50)
    code = models.CharField(max_length=60)

    def __str__(self):
        return self.username
