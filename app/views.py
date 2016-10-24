from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone
from django.views.generic import TemplateView

from car.models import Group


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = "platform/home.html"

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['cars'] = self.request.user.driver.caraccess_set.filter(start_time__lte=timezone.now()).exclude(end_time__lt=timezone.now())
        context['groups'] = Group.objects.filter(drivergroup__driver=self.request.user.driver)
        return context
