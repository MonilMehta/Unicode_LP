from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


# class UserForm(ModelForm):
#     class Meta:
#         model = Users
#         fields = '__all__'


class CreateUserForm(UserCreationForm):
    # image = forms.ImageField(upload_to="ToDoApp\static\images", blank=True, null=True)
    class Meta:
        model = User
        fields = ['username','email','password1','password2',]