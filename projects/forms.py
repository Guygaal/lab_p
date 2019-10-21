from django import forms
from .models import Task
from workers.models import Emp
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['text', 'name1', 'fond', 'foundation', 'start', 'finish', 'pr_type', 'pr_cost','pr_org', 'pr_also', 'pr_notes', 'pr_comments']
        labels = {'text': 'Название проекта'}


class AddEmps(forms.ModelForm):
    emp = Emp.objects.order_by('text')

    class Meta:
        model = Task
        fields = ['text']