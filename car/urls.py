from django.conf.urls import url

from car.views import CarDetail, CarUpdate, use_car

urlpatterns = [
    url(r'^detail$', CarDetail.as_view(), name="detail"),
    url(r'^edit/(?P<pk>[0-9]+)$', CarUpdate.as_view(), name="edit"),
    url(r'^use/(?P<pk>[0-9]+)$', use_car, name="use_car")
]
