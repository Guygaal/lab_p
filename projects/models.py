from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Task(models.Model):
    """Проект"""
#    emps = models.ManyToManyField('workers.Emp')
    text = models.CharField(max_length=200, blank=True, null=True, verbose_name='Название проекта')
    name1 = models.CharField(max_length=200, blank=True, null=True, verbose_name='Уникальный номер проекта')
    fond = models.CharField(max_length=200, blank=True, null=True, verbose_name='Фонд')
    foundation = models.CharField(max_length=200, blank=True, null=True, verbose_name='Основание для проведения проекта')
    start = models.CharField(max_length=200, blank=True, null=True, verbose_name='Дата начала проекта')
    finish = models.CharField(max_length=200, blank=True, null=True, verbose_name='Дата конца проекта')
    pr_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='Тип проекта')
    pr_cost = models.CharField(max_length=200, blank=True, null=True, verbose_name='Полная сумма проекта')
    pr_org = models.CharField(max_length=200, blank=True, null=True, verbose_name='Организация')
    pr_also = models.CharField(max_length=200, blank=True, null=True, verbose_name='Соисполнители')
    pr_notes = models.CharField(max_length=200, blank=True, null=True, verbose_name='Примечания')
    pr_comments = models.CharField(max_length=200, blank=True, null=True, verbose_name='Комментарии')
    date_added = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()
 #   owner = models.ForeignKey(User, on_delete=models.PROTECT)
    def __str__(self):
        """Возвращает строковое представление модели."""
        return self.text
