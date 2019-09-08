from django import forms

from .models import Task

class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ('user', 'name','start','days', 'created_date',)
