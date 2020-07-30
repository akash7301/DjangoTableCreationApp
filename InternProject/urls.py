"""InternProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from django.conf.urls import include, url
from TimeTableApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.sign_up_view,name='signup'),
    path('accounts/',include('django.contrib.auth.urls'),name='login'),
    path('main/',views.home_view, name='home'),
    path('createtable/',views.createTableView,name='create'),
    path('createdatatable', views.createDataTable,name='created'),
    path('Edittable/<int:pk>', views.editTableView, name='edittable'),
    path('update/<int:pk>',views.updateTable,name='updated'),
    path('delete/<int:pk>',views.deleteTable,name='deleted'),
    path('newtable',views.newTableView,name='new'),
]
