from django import forms
from .models import Vehicle, Chalan
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

        
class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = ['registration_number', 'owner_name', 'model', 'color', 'registration_date']


class ChalanForm(forms.ModelForm):
    class Meta:
        model = Chalan
        fields = ['chalan_date', 'amount', 'description']

