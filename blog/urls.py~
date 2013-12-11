# -*- coding: utf-8 -*-
from django.conf.urls import patterns,url

from blog import views

urlpatterns = patterns('',
    url(r'^$', views.blog_home, name="blog_home"),
    url(r'^Archive/$', views.blog_archive, name="blog_archive"),
    url(r'^Tags/$', views.blog_tags, name="blog_tags"),
    url(r'^Categories/$', views.blog_categories, name="blog_categories"),
    url(r'^Aboutme/$', views.blog_aboutme, name="blog_aboutme"),
    url(r'^WebAPPs/$', views.blog_webapps, name="blog_webapps"),
    url(r'^Markdown/$', views.blog_markdown, name="blog_markdown"),
    url(r'^Blog/(?P<slug>[-\w]+)$', views.blog_detail, name="blog_detail"),
    )
