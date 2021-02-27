"""securityflawsite URL Configuration

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
from django.contrib import admin, auth
from django.urls import include, path
from django.contrib.auth.views import LoginView, LogoutView
from pages import views
from securityflawsite import settings

#urlpatterns = []

#if settings.ADMIN_ENABLED is True:
#    urlpatterns += [path('admin/', admin.site.urls),]

urlpatterns = [
    path('pages/', include('pages.urls')),
    path('admin/', admin.site.urls),
    path('login/', LoginView.as_view(template_name='pages/login.html')),
    path('register/', views.register, name='register'),
	path('accounts/profile/logout/', LogoutView.as_view(template_name='pages/login.html')),
    path('logout/', LogoutView.as_view(next_page='/')),
    path('', include('pages.urls'))
]
