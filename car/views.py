from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.views.generic import DetailView, UpdateView

from car.models import Car


class CarDetail(LoginRequiredMixin, DetailView):
    template_name = "car/car_detail.html"
    model = Car


class CarUpdate(LoginRequiredMixin, UpdateView):
    template_name = "car/car_form.html"
    model = Car


def use_car(request, pk):
    Car.objects.filter(active_driver=request.user.driver).update(active_driver=None)
    car = Car.objects.get(pk=pk)
    car.active_driver = request.user.driver
    car.save()
    return redirect("platform:home")
