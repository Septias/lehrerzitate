from django.db import models
import datetime
# Create your models here.

class Teacher(models.Model):
    name = models.CharField('Name', max_length=40)

    def __str__(self):
        return self.name

class Quote(models.Model):
    published = models.DateField(auto_now_add=True)
    text = models.TextField('Zitat', max_length=400)
    teacher = models.ForeignKey(Teacher, models.CASCADE, related_name='quotes', verbose_name='Lehrer', blank=False)
    date = models.DateField('Datum', blank=True, null=True)

    def __str__(self):
        return self.text[:10] + '...'