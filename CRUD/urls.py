"""CRUD URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from app import views ,views1

urlpatterns = [
    path('admin/', admin.site.urls),

    # path('',views.add_show, name='add&show'),
    # path('delete/<int:id>/',views.delete_std, name='deletedata'),
    # path('update/<int:id>/',views.Update_Record, name='updaterecord'),

#   ==========================Class Base View====================================

    path('',views1.UserAddShowView.as_view(), name='add&show'),
    path('delete/<int:id>/',views1.UserDelete_View.as_view(), name='deletedata'),
    path('update/<int:id>/',views1.Update_Record.as_view(), name='updaterecord'),



]
