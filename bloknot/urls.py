"""bloknot URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from main.views import index, BlLoginView, BlRegisterUserView, BlLogoutView, edit_page, detail_page

urlpatterns = [
    path('', index, name='index'),
    path('admin/', admin.site.urls),
    path('login/', BlLoginView.as_view(), name='login_page'),
    path('register/', BlRegisterUserView.as_view(), name='register_page'),
    path('logout', BlLogoutView.as_view(), name='logout_page'),
    path('detail/<int:pk>', detail_page, name='detail_page'),
    path('edit/<int:pk>', edit_page, name='edit_page')
]
