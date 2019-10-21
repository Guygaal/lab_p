from django import forms
from .models import Emp
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from projects.models import Task


class EmpForm(forms.ModelForm):
    class Meta:
        model = Emp
        fields = ['text', 'name1', 'name2', 'spin', 'res_id', 'sc_id', 'inn', 'snils', 'birthday', 'passport']
        labels = {'text': 'Фамилия'}


class AddTasks(forms.ModelForm):
    task = Task.objects.order_by('text')

    class Meta:
        model = Emp
        fields = ['tasks']


'''class AddTasks(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['text']
        labels = {'text': 'Проект:'}
        widgets = {'text': forms.CheckboxSelectMultiple
                   }'''
