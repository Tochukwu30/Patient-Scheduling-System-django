"""pss URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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

# from django.conf.urls import url
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    # url(r"^rest-auth/", include("rest_auth.urls")),
    # url(r"^rest-auth/registration/", include("rest_auth.registration.urls")),
    path("auth/", include("auth_and_reg.urls", namespace="auth_and_reg")),
    path("appointments/", include("appointments.urls", namespace="appointments")),
    path("chats/", include("chat.urls", namespace="chat")),
]
