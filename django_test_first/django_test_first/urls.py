"""django_test_first URL Configuration

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
from django.urls import path, include
from django.conf.urls import url
import os
from django.conf import settings
from django.views.generic import TemplateView
from django.views.static import serve
from django.contrib.auth import views as auth_views

# from  django.conf.urls import url, include
# from test_two import views
BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE_ROOT = os.path.join(BASE_DIR, 'site')

urlpatterns = [
    # path(r'', include('helloworld.urls')),
    # path('', TemplateView.as_view(template_name='home/main.html')),
    path('', include('home.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    # path(r'', include('test_two.urls')),
    path('hello/', include('hello.urls')),
    path('polls/', include('polls.urls')),
    path('autos/', include('autos.urls')),
    path('cats/', include('cats.urls')),
    path('ads/', include('ads.urls')),
    url(r'^site/(?P<path>.*)$', serve, {'document_root': SITE_ROOT, 'show_indexes': True}, name='site_path'),
    path('accounts/', include('django.contrib.auth.urls')),  # Keep
    #url(r'^oauth/', include('social_django.urls', namespace='social')),  # Keep
]
urlpatterns += [
    url(r'^site/(?P<path>.*)$', serve,
        {'document_root': os.path.join(BASE_DIR, 'site'),
         'show_indexes': True},
        name='site_path'
        ),
]

# Serve the favicon - Keep for later
urlpatterns += [
    path('favicon.ico', serve, {
        'path': 'favicon.ico',
        'document_root': os.path.join(BASE_DIR, 'home/static'),
    }
         ),
]
try:
    from . import github_settings

    social_login = 'registration/login_social.html'
    urlpatterns.insert(0,
                       path('accounts/login/', auth_views.LoginView.as_view(template_name=social_login))
                       )
    print('Using', social_login, 'as the login template')
except:
    print('Using registration/login.html as the login template')
