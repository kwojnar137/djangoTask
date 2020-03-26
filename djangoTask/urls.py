"""djangoTask URL Configuration

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
from bizzfuzz.views import  (
    index,
    register,
    edit,
    delete,
    details,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index.as_view(), name='index'),
    path('<int:user_id>/details/', details, name='details'),
    path('register/', register, name='register'),
    path('<int:user_id>/edit/', edit, name='edit'),
    path('<int:user_id>/delete/', delete, name='delete'),
    
]