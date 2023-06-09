from app2.models import CustomUser,employee
from django import forms
from django.contrib.auth.forms import UserCreationForm
class CustomUserForm(UserCreationForm):
    class Meta:
        model=CustomUser
        fields=UserCreationForm.Meta.fields+('email','phone')

class employeeForm(forms.ModelForm):
    class Meta:
        model=employee
        fields='__all__'