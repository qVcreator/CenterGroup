from django.db import models
from django.urls import reverse


class Apartment(models.Model):
    square = models.CharField(max_length=50, verbose_name="Жилая площадь квартиры (кв.м.)")
    kitchen_square = models.CharField(max_length=50, verbose_name="Площадь кухни (кв.м)")
    balcony_square = models.CharField(max_length=50, verbose_name="Площадь балкона, если есть (кв.м) (По умолчанию: "
                                                                  "нет)")
    price = models.DecimalField(decimal_places=3, max_digits=12, verbose_name="Цена квартиры")
    price_punctuation = models.CharField(max_length=10, verbose_name="Валюта (По умолчанию: ₽)")
    address = models.CharField(max_length=255, verbose_name="Адрес квартиры")
    underground = models.CharField(max_length=255, verbose_name="Ближайшее метро")
    photos = models.ManyToManyField('ApartmentPhotos', null=True)
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Время изменения")

    def get_absolute_url(self):
        return reverse('apartment', kwargs={'apartment_id': self.pk})

    class Meta:
        verbose_name = 'Квартира'
        verbose_name_plural = 'Квартиры'
        ordering = ['-time_create']


class ApartmentPhotos(models.Model):
    # apartment = models.ForeignKey(Apartment, on_delete=models.PROTECT, verbose_name="Квартира")
    photo = models.ImageField(verbose_name="Фото")

    class Meta:
        verbose_name = 'Фото квартиры'
        verbose_name_plural = 'Фото квартиры'
