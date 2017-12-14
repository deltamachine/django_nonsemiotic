# -*- coding: utf-8 -*-

from django.contrib import admin
from django.forms import TextInput, Textarea, modelformset_factory
from django.db import models
from django.shortcuts import render
from .models import LanguagesData


admin.site.site_header = "Лексическая типология несемиотических жестов"
admin.site.site_title = "Редактирование данных"
admin.site.index_title = "Редактирование данных"


class LanguagesDataAdmin(admin.ModelAdmin):
    list_display = ['lang_code', 'gest', 'examp', 'constr', 'trans', 'comm']
    list_editable = ['gest', 'examp', 'constr', 'trans', 'comm']
    list_filter = ['lang']
    list_per_page = 102
    actions = None

    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'15'})},
        models.TextField: {'widget': Textarea(attrs={'rows':4, 'cols':40})},
    }


@admin.site.register_view('nonsemiotic/languagesdata/add/')
def my_view(request):
    def clean_fields(formset, fields):
        for field in fields:
            for i in range(len(formset[field])):
                formset[field][i].data['value'] = ""

        return formset

    Formset = modelformset_factory(LanguagesData, fields=('lang', 'lang_code', 'gest', 'examp', 'constr', 'trans', 'comm'), labels=None)
    formset = Formset()[:2]

    fields = ('lang', 'lang_code', 'examp', 'constr', 'trans', 'comm')
    #formset = clean_fields(formset, fields)

    return render(request, 'admin/nonsemiotic/change_form.html', {'formset': formset})

    
admin.site.register(LanguagesData, LanguagesDataAdmin)
