from django.contrib import admin
from . import models

# Register your models here.

class QuotesInline(admin.StackedInline):
    model = models.Quote
    extra = 0

@admin.register(models.Teacher)
class AdminTeacher(admin.ModelAdmin):
    inlines = [QuotesInline]

admin.site.register(models.Quote)