from django.conf.urls import url
from . import views

app_name='vote'

urlpatterns=[
    url(r'^login/$',views.login,name='login'),
    url(r'^lonout/$',views.logout,name='logout'),
    url(r'^index/$',views.index,name='index'),
    url(r'^detail/(\d+)/$',views.detail,name='detail'),
    url(r'^result/(\d+)/$',views.result,name='result')
]
