
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView
from django.contrib import admin
from django.urls import path
from k_app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('kcam/', views.kcam, name='cam'),
    path('result/', views.result, name='output'), #NEW
    path('admin/', admin.site.urls),
    path('favicon.ico', views.favicon),
]
