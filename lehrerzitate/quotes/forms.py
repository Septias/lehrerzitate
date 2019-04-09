from django.forms import ModelForm
from .models import Quote, Report
from django.forms import Textarea
from bootstrap_datepicker_plus import YearPickerInput
from django.utils.translation import gettext_lazy as _

class QuoteForm(ModelForm):
    class Meta:
        model = Quote
        fields = ['teacher', 'text', 'year']
        
        help_texts = {
            'year': _('not required'),
        }
        widgets = {
            'text': Textarea(attrs={'cols': 80, 'rows': 3}),
            'year': YearPickerInput(format='20%y')
        }

class ReportForm(ModelForm):
    class Meta:
        model = Report
        fields = '__all__'