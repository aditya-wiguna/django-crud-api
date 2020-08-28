from django.conf.urls import url
from customer import views

urlpatterns = [
    url(r'^api/customer$', views.index),
    url(r'^api/customer/(?P<pk>[0-9]+)$', views.show)
]