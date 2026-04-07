"""
URL configuration for Zeryons project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from Admin_panel import views

urlpatterns = [
    path('', views.Admin, name='Admin'),
    path('main', views.Main, name='Main'),
    path('header', views.Header, name='Header'),
    path('sidebar', views.Sidebar, name='Sidebar'),
    path('admin_login_zeryons', views.admin_login_zeryons, name='admin_login_zeryons'),
    path('admin_logout_zeryons', views.admin_logout_zeryons, name='admin_logout_zeryons'),
    path('basicform', views.Basic_Form, name='Basic_Form'),
    path('basictable', views.Basic_Table, name='Basic_Table'),
    path('contacttable', views.Contact_Table, name='Contact_Table'),
]


