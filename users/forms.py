from django import forms

from users.models import User
from users.validators import validate_password

class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

class UserRegisterForm(StyleFormMixin, forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat the password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email',)
    
    def clean_password2(self):
        cd = self.cleaned_data
        validate_password(cd['password'])
        if cd['password'] != cd['password2']:
            print('The passwords do not match.')
            raise forms.ValidationError('The passwords do not match.', code='invalid')
        return cd['password']

class UserLoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

class UserForm(forms.Form):
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'phone',)

class UserUpdateForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'phone', 'telegram', 'avatar')
