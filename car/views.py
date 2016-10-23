from django.views.generic import DetailView, UpdateView


class CarDetail(DetailView):
    template_name = "car/car_detail.html"


class CarUpdate(UpdateView):
    template_name = "car/car_form.html"
