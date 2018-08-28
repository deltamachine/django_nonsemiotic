from django.conf.urls import include, url
from django.contrib import admin
#from adminplus.sites import AdminSitePlus
from nonsemiotic.views import MainView, AboutProjectView, PublicationsView, SearchView
from django.conf.urls.i18n import i18n_patterns
from django.conf import settings
from django.conf.urls.static import static

#admin.site = AdminSitePlus()
#admin.autodiscover()

#urlpatterns = []

urlpatterns = [
    url(r'^$', MainView.as_view(), name='index'),
    url(r'^about_project$', AboutProjectView.as_view(), name='project'),
    url(r'^publications$', PublicationsView.as_view(), name='publications'),
    url(r'^search$', SearchView.as_view(), name='search'),
    url(r'^i18n/', include('django.conf.urls.i18n'), name='set_language'),
]

urlpatterns += i18n_patterns(
    url(r'^$', MainView.as_view(), name='index'),
    url(r'^about_project$', AboutProjectView.as_view(), name='project'),
    url(r'^publications$', PublicationsView.as_view(), name='publications'),
    url(r'^search$', SearchView.as_view(), name='search'),
    url(r'^i18n/', include('django.conf.urls.i18n'), name='set_language'),
)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
