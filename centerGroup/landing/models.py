from django.db import models


class Apartament(models.Model):
    square = models.CharField(max_length=50, verbose_name="Жилая площадь квартиры (кв.м.)")
    kitchen_square = models.CharField(max_length=50, verbose_name="Площадь кухни (кв.м)")
    balcony_square = models.CharField(max_length=50, verbose_name="Площадь балкона, если есть (кв.м) (По умолчанию: "
                                                                  "нет)")
    price = models.DecimalField(verbose_name="Цена квартиры")
    price_punctuation = models.CharField(max_length=10, verbose_name="Валюта (По умолчанию: ₽)")
    address = models.CharField(max_length=255, verbose_name="Адрес квартиры")
    underground = models.CharField(max_length=255, verbose_name="Ближайшее метро")

