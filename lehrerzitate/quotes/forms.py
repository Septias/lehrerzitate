from django.forms import ModelForm
from .models import Quote
from django.forms import Textarea
from bootstrap_datepicker_plus import DatePickerInput

class QuoteForm(ModelForm):
    class Meta:
        model = Quote
        fields = ['teacher', 'text', 'date']
        widgets = {
            'text': Textarea(attrs={'cols': 80, 'rows': 3}),
            'date': DatePickerInput(format='%Y-%m-%d')
        }

