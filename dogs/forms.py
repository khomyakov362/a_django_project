import datetime
from django import forms

from dogs.models import Dog, DogParent
from users.forms import StyleFormMixin

class DogForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Dog
        exclude = ('owner', 'is_active', 'views')
    
    def clean_birth_date(self):
        cd = self.cleaned_data['birth_date']
        if cd:
            now_year = datetime.datetime.now().year
            if now_year - cd.year > 35:
                raise forms.ValidationError('The dog must be younger than 35 years.')
        return cd

class ParentForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = DogParent
        fields = '__all__'