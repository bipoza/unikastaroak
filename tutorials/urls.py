from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.article_list, name='article_list'),
    url(r'^article/(?P<pk>[0-9]+)/$', views.article_detail, name='article_detail'),
    url(r'^article/new/$', views.article_new, name='article_new'),
    url(r'^article/(?P<pk>[0-9]+)/edit/$', views.article_edit, name='article_edit'),
    url(r'^article/user/(?P<username>[a-zA-Z0-9]+)$', views.user_articles, name='user_articles'),
    url(r'^drafts/$', views.article_draft_list, name='article_draft_list'),
    url(r'^article/(?P<pk>\d+)/remove/$', views.article_remove, name='article_remove'),
    url(r'^article/(?P<pk>\d+)/publish/$', views.article_publish, name='article_publish'),
    url(r'^categories/$', views.categories_list, name='categories_list'),
    url(r'^accounts/register/$', views.signup, name='register'),
    url(r'^accounts/profile/(?P<username>[a-zA-Z0-9]+)$', views.profile, name='profile'),
    url(r'^categories/article_list/(?P<categoryParam>[a-zA-Z0-9]+)$', views.article_list_category, name='article_list_catergory'),
    ]