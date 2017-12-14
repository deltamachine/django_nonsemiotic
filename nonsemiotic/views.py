# -*- coding: utf-8 -*-

from django.db import models
from django.db.models import Q
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import View, TemplateView
from django.utils.translation import ugettext as _
from .models import LanguagesData
from functools import reduce
from operator import __or__ as OR


class MainView(TemplateView):
    template_name = 'nonsemiotic/main.html'


class AboutProjectView(TemplateView):
    template_name = 'nonsemiotic/about_project.html'


class PublicationsView(TemplateView):
    template_name = 'nonsemiotic/publications.html'


class SearchView(View):
    def collect_template_data(self):
        languages = LanguagesData.objects.values('lang', 'lang_code').distinct().order_by('lang')
        gestures = LanguagesData.objects.filter(lang_code='est').values('gest', 'num').order_by('num')

        feet = gestures[:25]
        hands = gestures[25:71]
        back = gestures[71:76]
        head = gestures[76:84]
        other = gestures[84:]

        return languages, feet, hands, back, head, other

    def get_data_from_db(self, parameters):
        search_for_lang = [Q(lang_code=lang) for lang in parameters.getlist('lang')]
        search_for_gest = [Q(num=gest) for gest in parameters.getlist('part')]

        result = LanguagesData.objects.filter(reduce(OR, search_for_lang), 
          reduce(OR, search_for_gest)).values('lang', 'gest', 'examp', 'constr', 'trans', 'comm')

        return result

    def get(self, request):
        languages, feet, hands, back, head, other = self.collect_template_data()
        print(languages)
        
        if request.GET:
            try:
                result = self.get_data_from_db(request.GET)
                return render(request, 'nonsemiotic/results.html', {'result': result})
            except:
                pass

        return render(request,
                      'nonsemiotic/search.html',
                      {'langs': languages,
                       'feet': feet,
                       'hands': hands,
                       'back': back,
                       'head': head,
                       'other': other})
