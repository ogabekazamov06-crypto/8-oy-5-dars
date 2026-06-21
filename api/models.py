from django.db import models

class CarBrand(models.Model):
    name = models.CharField(max_length=255, verbose_name="Nomi")
    country =models.CharField(max_length=100, verbose_name="shahri")

    def __str__(self):
        return self.name



class Car(models.Model):
    model_name = models.CharField(max_length=100, verbose_name="Model nomi")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Narxi")
    color = models.CharField(max_length=50, verbose_name="Rangi")
    year = models.IntegerField()
    brand = models.ForeignKey(CarBrand, on_delete=models.CASCADE, verbose_name="Brandi")


    def __str__(self):
       return f"{self.brand.name} {self.model_name}"


class Comment(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.author.username} - {self.car.model_name}"