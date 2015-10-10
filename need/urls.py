from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^(?P<pk>[0-9]+)/$', views.detail, name='detail'),
	url(r'^new/$', views.new, name='new'),
	url(r'^(?P<pk>[0-9]+)/done$', views.done, name='done'),
	url(r'^(?P<pk>[0-9]+)/delete$', views.delete, name='delete'),
	url(r'^langchoice$', views.langchoice, name='langchoice'),
	url(r'^about/$', views.about, name='about'),
	url(r'^need/(?P<pk>[0-9]+)/transl/$', views.add_transl, name='add_transl'),
	url(r'^need/(?P<pk>[0-9]+)/transl/remove$', views.remove_transl, name='remove_transl'),
]
