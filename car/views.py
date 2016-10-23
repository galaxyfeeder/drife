from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, UpdateView


class CarDetail(LoginRequiredMixin, DetailView):
    template_name = "car/car_detail.html"


class CarUpdate(LoginRequiredMixin, UpdateView):
    template_name = "car/car_form.html"
