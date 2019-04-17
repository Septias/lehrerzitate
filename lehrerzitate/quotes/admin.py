from django.contrib import admin
from . import models

# Register your models here.

class QuotesInline(admin.StackedInline):
    model = models.Quote
    extra = 0

@admin.register(models.Teacher)
class AdminTeacher(admin.ModelAdmin):
    inlines = [QuotesInline]


class AdminQuote(admin.ModelAdmin):
    list_display = ('text', 'teacher', 'published')

admin.site.register(models.Quote, AdminQuote)
admin.site.register(models.Report)