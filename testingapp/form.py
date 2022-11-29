from django import forms
from testingapp.models import TodoListModel

class TaskForm(forms.ModelForm):
    class Meta:
        model = TodoListModel
        fields = ['task','done']