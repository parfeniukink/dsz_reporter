from django.contrib import admin

from core.models import Report, Url


@admin.register(Url)
class UrlAdmin(admin.ModelAdmin):
    pass


@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = ["date", "time", "url", "status"]
    search_fields = ["date", "url"]
