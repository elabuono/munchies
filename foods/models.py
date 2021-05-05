from django.db import models


class Cuisine(models.Model):
    cuisine_type = models.CharField(max_length=200)
    def __str__(self):
        return self.cuisine_type

class Food(models.Model):
    cuisine_type = models.ForeignKey(Cuisine, null=True, on_delete=models.CASCADE)
    food_text = models.CharField(max_length=200)
    def __str__(self):
        return self.food_text
