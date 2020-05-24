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
    url(r'^registration$', app.views.registration, name='registration'), #регистрация    #
    url('login/',LoginView.as_view(template_name = 'app/login.html' ,authentication_form = app.forms.BootstrapAuthenticationForm), name = 'login'),
    url('logout/',LogoutView.as_view(template_name = 'app/index.html',next_page='/'), name='logout'),     #4-5 работа    url(r'^blog$', app.views.blog, name='blog'),    url(r'^(?P<id>\d+)/$', app.views.blogpost, name='blogpost'),    #6работа    url(r'^newpost$',app.views.newpost, name = 'newpost'),    url(r'^menu$', app.views.menu, name='menu'),    url(r'^cart/$', app.views.cart_view, name='cart'),    url(r'^add_to_cart/$', app.views.add_to_cart_view, name='add_to_cart'),    url(r'^remove_from_cart/$', app.views.remove_from_cart_view, name='remove_from_cart'),    url(r'^change_item_qty/$', app.views.change_item_qty, name="change_item_qty"),    url(r'^product/(?P<product_slug>[-\w]+)/$', app.views.product_view, name='product_detail'),    url(r'^category/(?P<category_slug>[-\w]+)/$', app.views.category_view, name='category_detail'),    url(r'checkout/$', app.views.checkout_view, name='checkout'),    url(r'order/$', app.views.order_create_view, name='create_order'),    url(r'my-orders/$', app.views.client_orders, name='client_orders'),    url(r'user-orders/$', app.views.manager_orders, name='manager_orders'),    url(r'^delete-order/(?P<id>\d+)/$', app.views.delete_order, name='delete_order'),    url(r'^edit-order/(?P<id>\d+)/$', app.views.edit_order, name='edit_order'),    ]#6лаба?  загруженные через формы файлы, будут сохраняться в папке mediaurlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()if settings.DEBUG:    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)