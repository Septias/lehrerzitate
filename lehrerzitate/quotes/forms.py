from django.forms import ModelForm
from .models import Quote
from django.forms import Textarea

class QuoteForm(ModelForm):
    class Meta:
        model = Quote
        fields = ['teacher', 'text']
        widgets = {
            'text': Textarea(attrs={'cols': 80, 'rows': 3}),
        }

    def __init__(self, *args, **kwargs):
        super(QuoteForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'