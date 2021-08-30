from django.urls import path, re_path
from . import views

urlpatterns = [
    path(r'', views.home),
    path(r'items', views.items),
    re_path(r'items/([0-9]{4}/$)', views.items_num),
    re_path(r'items/(?P<year>[\d]{4})/(?P<month>[\d]{2})/(?P<day>[\d]{2})/$', views.items_day),
    re_path(r'book/$', views.book_page),
    re_path(r'book/(?P<page>[0-9]+)/$', views.book_page)
]
