from django import forms
from django.contrib.auth.models import User
from .models import Table



class SignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username','password')
        #widgets = {'password': forms.PasswordInput(),}
    def clean(self):
        cleaned_data = super(SignUpForm, self).clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError("password and confirm password does not match!")
class TableForm(forms.ModelForm):
    class Meta:
        model = Table
        fields = ['table_data']
