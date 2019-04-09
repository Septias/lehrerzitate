from django.db import models
import datetime
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_year(year):
    if not (year > 2000 and year <= datetime.datetime.now().year):
        raise ValidationError(
            _('%(year)s is not between 2000 and 2019'),
            params={'year': year}
        )


class Teacher(models.Model):
    name = models.CharField('Name', max_length=40, unique = True)

    def __str__(self):
        return self.name

class Quote(models.Model):
    published = models.DateField(auto_now_add=True)
    text = models.TextField('Zitat', max_length=400, unique=True)
    teacher = models.ForeignKey(Teacher, models.CASCADE, related_name='quotes', verbose_name='Lehrer', blank=False)
    year = models.IntegerField('Datum', blank=True, null=True, default=datetime.datetime.now().year, validators=[validate_year])

    def __str__(self):
        return self.text[:50] + '...'

class Report(models.Model):
    quote = models.ForeignKey(Quote, on_delete=models.CASCADE, verbose_name = 'Zitat')
    reason = models.TextField('Grund', max_length=700)
    email = models.EmailField('Email')
    