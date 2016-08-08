from django.conf.urls import url

import views

urlpatterns = [

    url(r'^$', views.index, name='index'),
    url(r'^retrieve', views.retrieve_item, name='retrieve'),
]
