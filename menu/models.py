from django.db import models


class Menu(models.Model):
    dish_name = models.CharField(max_length=50)
    dish_image = models.ImageField(upload_to='dishes/')
    dish_description = models.TextField()
    dish_ingredients = models.TextField()

    def __str__(self):
        return self.dish_name
