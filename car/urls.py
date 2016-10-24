from django.conf.urls import url

from car.views import CarDetail, CarUpdate, use_car, get_driver_data, finish_using_car

urlpatterns = [
    url(r'^detail$', CarDetail.as_view(), name="detail"),
    url(r'^edit/(?P<pk>[0-9]+)$', CarUpdate.as_view(), name="edit"),
    url(r'^use/(?P<pk>[0-9]+)$', use_car, name="use_car"),
    url(r'^auth/driver$', get_driver_data, name="driver_data"),
    url(r'^auth/finish$', finish_using_car, name="finish_use")
]
