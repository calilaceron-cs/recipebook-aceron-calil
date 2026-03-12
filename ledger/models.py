from django.db import models
from django.urls import reverse

from accounts.models import Profile


class Ingredient(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("ledger:ingredient-detail", args=[self.pk])


class Recipe(models.Model):
    name = models.CharField(max_length=100)
    author = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name='recipes',
        null=True
    )
    created_on = models.DateField(auto_now_add=True, null=True)
    updated_on = models.DateField(auto_now=True, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("ledger:recipe-detail", args=[self.pk])


class RecipeIngredient(models.Model):
    quantity = models.CharField(max_length=100)

    ingredient = models.ForeignKey(
        Ingredient,
        on_delete=models.CASCADE,
        related_name='recipe',
    )

    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='ingredients',
    )

    def __str__(self):
        return f"{self.ingredient}"


class RecipeImage(models.Model):
    image = models.ImageField(
        upload_to="images/",
        null=True
    )
    description = models.CharField(
        max_length=255
    )
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='images'
    )

    def get_absolute_url(self):
        return reverse("ledger:recipe-detail", args=[self.recipe.pk])
