from django.db import models


class Car(models.Model):
    CAR_TYPE = (
        ("Седан", "Седан"),
        ("Купе", "Купе"),
        ("Универсал", "Универсал")
    )

    title = models.CharField("Напишите название машины", max_length=100, help_text="Максимум 100 символов")
    description = models.TextField("Напишите описание")
    image = models.ImageField(upload_to="")
    car_type = models.CharField("Тип машины", max_length=100, choices=CAR_TYPE)
    created_date = models.DateTimeField(auto_now_add=True)
    price = models.PositiveIntegerField("Цена")
    video = models.URLField("Видео")

    def __str__(self):
        return self.title
