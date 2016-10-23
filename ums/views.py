from django.views.generic import DetailView, UpdateView


class DriverDetail(DetailView):
    template_name = "ums/driver_detail.html"


class DriverUpdate(UpdateView):
    template_name = "ums/driver_form.html"
