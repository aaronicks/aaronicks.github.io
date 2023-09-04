"""demosrc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from product.views import laptop_view, about_view, contact_view, laptops_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('laptop/', laptop_view, name="laptop"),
    path('about/', about_view, name="about"),
    path('contact/', contact_view, name="contact"),
    path('create/', laptops_view, name="create"),
]
