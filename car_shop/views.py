from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView

from .models import Car, CommentCar
from .forms import CarForm, CommentFrom
from django.http import HttpResponse


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


# предварительный просмотр
def car_list_view(request):
    car_objects = Car.objects.all()
    return render(request, "car_list.html", {'car_objects': car_objects})

# детальный просмотр
def car_detail_view(request, id):
    car_detail = get_object_or_404(Car, id=id)
    return render(request, "car_detail.html", {"car_detail": car_detail})


# добавление машины
def create_car_view(request):
    method = request.method
    if method == "POST":
        form = CarForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse("<h2>Машина успешно добавлена</h2>")
    else:
        form = CarForm()
    return render(request, 'create_car.html', {"form": form})


# обновление машины
def update_object_view(request, id):
    car_object = get_object_or_404(Car, id=id)
    if request.method == "POST":
        form = CarForm(instance=car_object, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("<h2>Машина успешно обновлена</h2>")
    else:
        form = CarForm(instance=car_object)
        return render(request, 'update_car.html', {"form": form,
                                                   "object": car_object
                                                   })


# удаление машины
def delete_object_view(request, id):
    car_object = get_object_or_404(Car, id=id)
    car_object.delete()
    return HttpResponse("<h2>Машина успешно удалена из базы данных</h2>")
