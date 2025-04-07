import datetime
from django import forms

from dogs.models import Dog
from users.forms import StyleFormMixin

class DogForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Dog
        exclude = ('owner',)
    
    def clean_birth_date(self):
        cd = self.cleaned_data['birth_date']
        now_year = datetime.datetime.now().year
        if now_year - cd.year > 35:
            raise forms.ValidationError('The dog must be younger than 35 years.')
        return cd
