from django.urls import path
from . import views

urlpatterns = [
    path('car_list/', views.car_list_view, name="car_list"),
    path('car_list/<int:id>/', views.car_detail_view, name="car_detail"),
    path('create_car/', views.create_car_view, name="create"),
]