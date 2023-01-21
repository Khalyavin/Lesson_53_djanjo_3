from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание')
    photo = models.ImageField(upload_to='image/', **NULLABLE)
    price = models.FloatField(verbose_name='Цена')
    date_org = models.DateField(verbose_name='Дата создания')
    date_fill = models.DateField(verbose_name='Дата заполнения')
    category_id = models.ForeignKey('Category', verbose_name='Категория', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name='Категория')
    description = models.TextField(verbose_name='Описание')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Продукты'


    def __str__(self):
        return self.name
