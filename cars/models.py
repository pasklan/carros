from django.db import models


class Car(models.Model):
    model = models.CharField('Modelo', max_length=100)
    brand = models.ForeignKey("cars.Brand", verbose_name="Marca",
                              on_delete=models.PROTECT, related_name='car_brand')
    factory_year = models.PositiveIntegerField(
        'Ano Fabricação', blank=True, null=True)
    plate = models.CharField("Placa", max_length=50, blank=True, null=True)
    model_year = models.PositiveIntegerField(
        'Ano Modelo', blank=True, null=True)
    value = models.FloatField('Valor', blank=True, null=True)
    photo = models.ImageField(
        upload_to='cars/img/', blank=True, null=True)
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.model


class Brand(models.Model):
    name = models.CharField("Nome", max_length=50)

    def __str__(self):
        return self.name


class CarInventory(models.Model):
    cars_count = models.IntegerField()
    cars_value = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']


    def __str__(self):
        return f'{self.cars_count} - {self.cars_value}'
