from django.urls import path
from . import views

urlpatterns = [
    path('car_list/', views.CarListView.as_view(), name="car_list"),
    path('car_list/<int:id>/', views.CarDetailView.as_view(), name="car_detail"),
    path('create_car/', views.CreateCarView.as_view(), name="create"),
    path('car_list/<int:id>/update/', views.CarUpdateView.as_view(), name="car_update"),
    path('car_list/<int:id>/delete/', views.CarDeleteView.as_view(), name="car_delete"),
    path('car_list/<int:id>/comment/', views.CarCommentView.as_view(), name="car_comment"),

]