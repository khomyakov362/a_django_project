from django import forms
from django.contrib.auth.forms import PasswordChangeForm, UserCreationForm, AuthenticationForm

from users.models import User
from users.validators import validate_password

class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

class UserRegisterForm(StyleFormMixin, UserCreationForm):
    class Meta:
        model = User
        fields = ('email',)
    
    def clean_password2(self):
        cd = self.cleaned_data
        validate_password(cd['password1'])
        if cd['password1'] != cd['password2']:
            print('The passwords do not match.')
            raise forms.ValidationError('The passwords don\'t match.', code='invalid')
        return cd['password2']

class UserLoginForm(StyleFormMixin, AuthenticationForm):
    pass

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'phone', 'avatar')

class UserUpdateForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'phone', 'telegram', 'avatar')

class UserChangePasswordForm(StyleFormMixin, PasswordChangeForm):
    pass

