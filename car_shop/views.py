from django.shortcuts import render, get_object_or_404
from .models import Car
from .forms import CarForm
from django.http import HttpResponse

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


