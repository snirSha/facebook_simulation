from django.urls import path,include
from . import views
from django.conf.urls import url


urlpatterns = [
    path('waiting/', views.waiting, name='facebook-waiting'),
    path('ready/', views.ready, name='facebook-ready'),
    path('end/', views.end, name='facebook-end'),
    path('home/', views.home, name='facebook-home'),
    path('create_post/', views.create_post, name='facebook-create-post'),
    url(r'^connent/(?P<operation>.+)/(?P<pk>\w+)/$', views.manage_friends, name='manage_friends'),
    url(r'^like/$',views.like_post, name='like_post'),
]


