from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from .forms import CarForm, CommentFrom
from .models import Car, CommentCar


# предварительный просмотр

class CarListView(ListView):
    template_name = 'car_list.html'
    queryset = Car.objects.all()

    def get_queryset(self):
        return Car.objects.all()


# def car_list_view(request):
#     car_objects = Car.objects.all()
#     return render(request, "car_list.html", {'car_objects': car_objects})

# детальный просмотр по id

class CarDetailView(DetailView):
    template_name = 'car_detail.html'

    def get_object(self, **kwargs):
        car_id = self.kwargs.get('id')
        return get_object_or_404(Car, id=car_id)


# def car_detail_view(request, id):
#     car_detail = get_object_or_404(Car, id=id)
#     return render(request, "car_detail.html", {"car_detail": car_detail})


# добавление машины

class CreateCarView(CreateView):
    template_name = 'create_car.html'
    form_class = CarForm
    queryset = Car.objects.all()
    success_url = '/car_list/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(CreateCarView, self).form_valid(form=form)


# def create_car_view(request):
#     method = request.method
#     if method == "POST":
#         form = CarForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponse("<h2>Машина успешно добавлена</h2>")
#     else:
#         form = CarForm()
#     return render(request, 'create_car.html', {"form": form})


# обновление машины

class CarUpdateView(UpdateView):
    template_name = 'update_car.html'
    form_class = CarForm
    success_url = '/car_list/'

    def get_object(self, **kwargs):
        car_id = self.kwargs.get('id')
        return get_object_or_404(Car, id=car_id)

    def form_valid(self, form):
        return super(CarUpdateView, self).form_valid(form=form)

# def update_object_view(request, id):
#     car_object = get_object_or_404(Car, id=id)
#     if request.method == "POST":
#         form = CarForm(instance=car_object, data=request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponse("<h2>Машина успешно обновлена</h2>")
#     else:
#         form = CarForm(instance=car_object)
#         return render(request, 'update_car.html', {"form": form,
#                                                    "object": car_object
#                                                    })


# удаление машины

class CarDeleteView(DeleteView):
    template_name = 'car_delete.html'
    success_url = "/car_list/"

    def get_object(self, **kwargs):
        car_id = self.kwargs.get('id')
        return get_object_or_404(Car, id=car_id)

# def delete_object_view(request, id):
#     car_object = get_object_or_404(Car, id=id)
#     car_object.delete()
#     return HttpResponse("<h2>Машина успешно удалена из базы данных</h2>")


class CarCommentView(CreateView):
    template_name = 'car_comment.html'
    form_class = CommentFrom
    queryset = CommentCar.objects.all()
    success_url = '/car_list/'

    def get_object(self, **kwargs):
        car_id = self.kwargs.get("id")
        return get_object_or_404(CommentCar, id=car_id)

    def form_valid(self, form):
        print(form.clean)
        return super(CarCommentView, self).form_valid(form=form)
