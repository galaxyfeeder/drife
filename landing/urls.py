from django.conf.urls import include, url
from django.contrib import admin

from landing.views import LandingView

urlpatterns = [
    url(r'^$', LandingView.as_view(), name="landing")
]
