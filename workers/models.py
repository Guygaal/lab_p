from django.db import models
from django.contrib.auth.models import User
from projects.models import Task
# Create your models here.


class Emp(models.Model):
    """Проект"""
    tasks = models.ManyToManyField(Task)
    leader = models.BooleanField(default=False)
    text = models.CharField(max_length=200, blank=True, null=True, verbose_name='Фамилия')
    name1 = models.CharField(max_length=200, blank=True, null=True, verbose_name='Имя')
    name2 = models.CharField(max_length=200, blank=True, null=True, verbose_name='Отчество')
    spin = models.CharField(max_length=200, blank=True, null=True, verbose_name='SPIN')
    res_id = models.CharField(max_length=200, blank=True, null=True, verbose_name='Researcher ID')
    sc_id = models.CharField(max_length=200, blank=True, null=True, verbose_name='Идентификатор учёного в ИС')
    inn = models.CharField(max_length=200, blank=True, null=True, verbose_name='ИНН')
    snils = models.CharField(max_length=200, blank=True, null=True, verbose_name='СНИЛС')
    birthday = models.CharField(max_length=200, blank=True, null=True, verbose_name='Дата рождения')
    passport = models.CharField(max_length=200, blank=True, null=True, verbose_name='Паспорт')
    date_added = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()
 #   owner = models.ForeignKey(User, on_delete=models.PROTECT)
    def __str__(self):
        """Возвращает строковое представление модели."""
        return self.text