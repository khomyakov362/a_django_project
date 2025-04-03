from django import forms

from users.models import User

class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat the password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email',)
    
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('The passwords do not match.')
        return cd['password']
