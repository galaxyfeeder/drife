from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
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


def get_driver_data(request):
    car = Car.objects.filter(license_plate=request.GET.get('license_plate', None)).first()
    if car and car.active_driver:
        return JsonResponse({'success': True, 'driver': {'name': car.active_driver.user.get_full_name(),
                                                         'alcoholemic_tax': car.active_driver.alcoholemic_tax}})
    else:
        return JsonResponse({'success': False})


def finish_using_car(request):
    car = Car.objects.filter(license_plate=request.GET.get('license_plate', None)).first()
    if car and car.active_driver:
        car.active_driver = None
        car.save()
        return JsonResponse({'success': True})
    else:
        return JsonResponse({'success': False})
