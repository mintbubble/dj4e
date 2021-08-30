from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path(r'', views.show)
    # url(regex=r'', view=views.show )
]
