from django.contrib import admin
from ru.models import UserInfo, About
from search.models import Report, Committee, ResetCode


class ProductAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'slug', 'alumni']

    class Meta:
        model = UserInfo


admin.site.register(UserInfo, ProductAdmin)


class ReportAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'report', 'status']

    class Meta:
        model = Report


class CommitteeAdmin(admin.ModelAdmin):
    list_display = ['year', 'active']

    class Meta:
        model = Committee


class ResetCodeAdmin(admin.ModelAdmin):
    list_display = ['username', 'code']

    class Meta:
        model = ResetCode


admin.site.register(Report, ReportAdmin)
admin.site.register(Committee, CommitteeAdmin)
admin.site.register(ResetCode, ResetCodeAdmin)
admin.site.register(About)
