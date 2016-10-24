from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.shortcuts import redirect
from django.utils import timezone
from django.views.generic import DetailView, UpdateView

from car.models import Car, CarUsage


class CarDetail(LoginRequiredMixin, DetailView):
    template_name = "car/car_detail.html"
    model = Car

    def get_context_data(self, **kwargs):
        context = super(CarDetail, self).get_context_data(**kwargs)
        context['last_usages'] = CarUsage.objects.filter(car=self.object)[:10]
        return context


class CarUpdate(LoginRequiredMixin, UpdateView):
    template_name = "car/car_form.html"
    model = Car


def use_car(request, pk):
    active_usages = CarUsage.objects.filter(end_time=None, driver=request.user.driver)
    if not active_usages:
        Car.objects.filter(active_driver=request.user.driver).update(active_driver=None)
        car = Car.objects.get(pk=pk)
        car.active_driver = request.user.driver
        car.save()
        CarUsage.objects.create(driver=request.user.driver, start_time=timezone.now(), car=car)
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
        CarUsage.objects.filter(end_time=None, driver=request.user.driver).update(end_time=timezone.now())
        return JsonResponse({'success': True})
    else:
        return JsonResponse({'success': False})
