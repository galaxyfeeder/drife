from django.conf.urls import url

from car.views import CarDetail, CarUpdate

urlpatterns = [
    url(r'^detail$', CarDetail.as_view(), name="detail"),
    url(r'^edit$', CarUpdate.as_view(), name="edit")
]
