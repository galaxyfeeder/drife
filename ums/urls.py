from django.conf.urls import url

from ums.views import DriverDetail, DriverUpdate, logout_view, LoginView

urlpatterns = [
    url(r'^detail$', DriverDetail.as_view(), name="driver_detail"),
    url(r'^edit$', DriverUpdate.as_view(), name="driver_edit"),
    url(r'^login$', LoginView.as_view(), name="login"),
    url(r'^logout$', logout_view, name="logout")
]
