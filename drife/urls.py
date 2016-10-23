from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include("app.urls", namespace="platform")),
    url(r'^driver/', include("ums.urls", namespace="ums"))
]
