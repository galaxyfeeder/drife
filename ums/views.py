from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.views.generic import DetailView, UpdateView, TemplateView

from ums.models import Driver


class DriverDetail(LoginRequiredMixin, DetailView):
    template_name = "ums/driver_detail.html"
    model = Driver

    def get_object(self, queryset=None):
        return self.request.user.driver


class DriverUpdate(LoginRequiredMixin, UpdateView):
    template_name = "ums/driver_form.html"
    model = Driver

    def get_object(self, queryset=None):
        return self.request.user.driver


class LoginView(TemplateView):
    template_name = "ums/login.html"

    def post(self, request, *args, **kwargs):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("platform:home")
        else:
            return self.render_to_response({'error': "Invalid auth."})


@login_required
def logout_view(request):
    logout(request)
    return redirect('platform:home')

