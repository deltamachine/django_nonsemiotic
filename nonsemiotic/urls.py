from django.conf.urls import url, include
from . import views
from .views import MainView, AboutProjectView, PublicationsView, SearchView


urlpatterns = [
    url(r'^$', MainView.as_view()),
    url(r'^about_project$', AboutProjectView.as_view()),
    url(r'^publications$', PublicationsView.as_view()),
    url(r'^search$', SearchView.as_view()),
    url(r'^i18n/', include('django.conf.urls.i18n')),
]