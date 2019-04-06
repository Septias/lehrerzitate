from django.forms import ModelForm
from .models import Quote
from django.forms import Textarea
from bootstrap_datepicker_plus import DatePickerInput
from django.utils.translation import gettext_lazy as _

class QuoteForm(ModelForm):
    class Meta:
        model = Quote
        fields = ['teacher', 'text', 'date']
        
        help_texts = {
            'date': _('not required'),
        }
        widgets = {
            'text': Textarea(attrs={'cols': 80, 'rows': 3}),
            'date': DatePickerInput(format='%Y-%m-%d')
        }

