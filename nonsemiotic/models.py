from __future__ import unicode_literals
from django.db import models


class LanguagesData(models.Model):
    num = models.IntegerField(blank=True, null=True)
    lang = models.CharField(max_length=255, blank=True, null=True)
    lang_code = models.CharField(max_length=255, blank=True, null=True, verbose_name="Язык")
    gest = models.CharField(max_length=255, blank=True, null=True, verbose_name="Пункт анкеты")
    examp = models.CharField(max_length=255, blank=True, null=True, verbose_name="Лексическое средство")
    constr = models.CharField(max_length=255, blank=True, null=True, verbose_name="Конструкция")
    trans = models.CharField(max_length=255, blank=True, null=True, verbose_name="Перевод")
    comm = models.CharField(max_length=255, blank=True, null=True, verbose_name="Комментарии")

    class Meta:
        verbose_name = 'языковые данные'
        verbose_name_plural = 'языковые данные'
        managed = False
        db_table = 'LanguagesData'
        ordering = ['lang_code', 'num']

    def __str__(self):
        return ('%s, %s' % (self.lang, self.gest))