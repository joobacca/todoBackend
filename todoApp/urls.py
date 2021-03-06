"""todoApp URL Configuration

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
from django.urls import path, re_path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_auth.registration.views import VerifyEmailView
from usermanagement.views import EmailConfirmationView

schema_view = get_schema_view(
    openapi.Info(
        title="TodoApp-API",
        default_version="v1",
        description="API of my hobby project",
        contact=openapi.Contact(email="joohankim@gmx.de"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,)
)

urlpatterns = [
    re_path(r'^$', schema_view.with_ui('swagger', cache_timeout=0), name='schema_redoc'),
    path('api/accounts/', include('allauth.urls')),
    re_path(r'^api/', include('django.contrib.auth.urls')),
    re_path(r"^api/auth/registration/account-confirm-email/(?P<key>[\s\d\w().+-_',:&]+)/$", EmailConfirmationView.as_view(), name='account_confirm_email'),
    re_path(r'^api/auth/registration/account-confirm-email/$', VerifyEmailView.as_view(), name='account_email_verification_sent'),
    path('api/auth/registration/', include('rest_auth.registration.urls')),
    path('api/auth/', include('rest_auth.urls')),
    path('api/todos/', include('todo.urls')),
    path('admin/', admin.site.urls),
]

