from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^platform/', include("app.urls", namespace="platform")),
    url(r'^accounts/', include("ums.urls", namespace="ums")),
    url(r'^car/', include("car.urls", namespace="car")),
    url(r'', include("landing.urls", namespace="landing"))
]
