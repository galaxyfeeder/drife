from django.conf.urls import url

from ums.views import DriverDetail, DriverUpdate

urlpatterns = [
    url(r'^detail$', DriverDetail.as_view(), name="driver_detail"),
    url(r'^edit$', DriverUpdate.as_view(), name="driver_edit")
]
