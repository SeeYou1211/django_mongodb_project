#!/usr/bin/python3
# -*- coding: utf-8 -*-
from django.conf.urls import include
from django.template.defaulttags import url
from rest_framework.urlpatterns import format_suffix_patterns

from tutorials import views

app_name = "tutorials"
# urlpatterns = [
#     path(r'snippets/', views.SnippetList.as_view()),
#     path(r'^snippets/(?P<pk>[0-9]+)/$', views.SnippetDetail.as_view()),
#     path(r'^snippets1/$', views.SnippetList1.as_view()),
#     path(r'^snippets1/(?P<pk>[0-9]+)/$', views.SnippetDetail1.as_view()),
#     path(r'^users/$', views.UserList.as_view()),
#     path(r'^users/^(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
#     # path('tutorials/published/', views.tutorial_list_published),
#     path(r'^$', views.api_root),
#     path(r'^snippets/(?P<pk>[0-9]+)/highlight/$', views.SnippetHighlight.as_view()),
#
# ]
from tutorials.views import SnippetViewSet, UserViewSet1, api_root
from rest_framework import renderers

snippet_list = SnippetViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
snippet_detail = SnippetViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})
snippet_highlight = SnippetViewSet.as_view({
    'get': 'highlight'
}, renderer_classes=[renderers.StaticHTMLRenderer])
user_list = UserViewSet1.as_view({
    'get': 'list'
})
user_detail = UserViewSet1.as_view({
    'get': 'retrieve'
})
