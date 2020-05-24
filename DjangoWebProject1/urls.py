"""
Definition of urls for DjangoWebProject1.
"""

from datetime import datetime
from django.conf.urls import url
import django.contrib.auth.views

#3 лаба

from django.contrib import admin #подключение дефолтной админки Django
from django.contrib.auth.views import LoginView, LogoutView #Дефолтные view для входа/выхода

#3 лаба
import app.views
import app.forms


#6лаба (импорт функций для настройки доступа кзагруженным файлам)
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.contrib import admin


# Uncomment the next lines to enable the admin:
from django.conf.urls import include
admin.autodiscover()

urlpatterns = [
    # Examples:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', app.views.home, name='home'),
    url(r'^contact$', app.views.contact, name='contact'),
    url(r'^about$', app.views.about, name='about'),
    url(r'^links$', app.views.links, name='links'),
    url(r'^xxx$', app.views.xxx, name='xxx'),
    url(r'^summer$', app.views.summer, name='summer'),
    url(r'^winter$', app.views.winter, name='winter'),
    url(r'^off_season$', app.views.off_season, name='off_season'),
    #3 работа
    url(r'^registration$', app.views.registration, name='registration'), #регистрация
    url('login/',LoginView.as_view(template_name = 'app/login.html' ,authentication_form = app.forms.BootstrapAuthenticationForm), name = 'login'),
    url('logout/',LogoutView.as_view(template_name = 'app/index.html',next_page='/'), name='logout'), 
urlpatterns += staticfiles_urlpatterns()