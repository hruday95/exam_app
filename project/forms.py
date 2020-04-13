from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    birth_date = forms.DateField(help_text='Required. Format: YYYY-MM-DD')
    father_name = forms.CharField(max_length= 40)
    e_mail = forms.CharField(max_length=30)
    current_address = forms.CharField(help_text="living now",max_length=200)
    permanent_address = forms.CharField(help_text='permanent',max_length=200)
    aadhar_card_number = forms.CharField(help_text='your registeredaadhar number')

    class Meta:
        model = User
        fields = ('username','first_name','last_name','birth_date', 'father_name','e_mail','password1', 'password2', )
