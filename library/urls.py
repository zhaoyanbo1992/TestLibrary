#!/usr/bin/env python
# -*- coding: utf-8 -*-


from django.urls import path
from library import views
from django.contrib.staticfiles import views as static_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
                  path('', views.index, name='index'),
                  path('login/', views.user_login, name='login'),
                  path('logout/', views.user_logout, name='logout'),
                  path('profile/', views.profile, name='profile'),
                  path('set_password/', views.set_password, name='set_password'),
                  path('static/(?P<path>.*)$', static_views.serve, name='static'),
                  path('book/detail$', views.book_detail, name='book_detail'),
                  path('book/action$', views.reader_operation, name='reader_operation'),
                  path('search/', views.book_search, name='book_search'),
                  path('statistics/', views.statistics, name='statistics'),
                  path('about/', views.about, name='about'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
