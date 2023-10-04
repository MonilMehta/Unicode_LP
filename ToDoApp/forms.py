from django.forms import ModelForm, Textarea
from .models import Tasks
from django.contrib.auth.models import User

class TasksForm(ModelForm):
    class Meta:
        model = Tasks
        fields = '__all__'
        widgets = {
            'description': Textarea(attrs={'rows': 4, 'cols': 20}),
        }