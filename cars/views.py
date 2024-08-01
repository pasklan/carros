from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from cars.models import Car
from cars.forms import CarModelForm
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


class CarListView(ListView):
    model = Car
    template_name = 'cars.html'
    context_object_name = 'cars'

    def get_queryset(self):
        queryset = super().get_queryset().order_by('model')
        search = self.request.GET.get('search')
        if search:
            queryset = queryset.filter(model__icontains=search)
        return queryset


class DetailCarView(DetailView):
    model = Car
    template_name = 'car_detail.html'


@method_decorator(login_required(login_url='login'), name='dispatch')
class NewCarCreateView(CreateView):
    template_name = "new_car.html"
    model = Car
    form_class = CarModelForm
    success_url = reverse_lazy('cars_list')


@method_decorator(login_required(login_url='login'), name='dispatch')
class CarUpdateView(UpdateView):
    model = Car
    form_class = CarModelForm
    template_name = 'car_update.html'

    def get_success_url(self):
        return reverse_lazy('detail_car', kwargs={ 'pk': self.object.pk })


@method_decorator(login_required(login_url='login'), name='dispatch')
class DeleteCarView(DeleteView):
    model = Car
    template_name = 'car_delete.html'
    success_url = '/cars/'