from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.


class Type(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    # db_index=True selfedu
    created_at = models.DateTimeField(default=timezone.now)
    # created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Restaurant(models.Model):
    title = models.CharField(max_length=200)
    place = models.CharField(max_length=200)
    note = models.CharField(max_length=900)
    image = models.ImageField(upload_to='restaurant/images/')
    # pri odstraneni Categorie, automaticky se odstrani vsechny restaurace v tomto Type
    # type = models.ForeignKey(Type, on_delete=models.CASCADE)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title


class Review(models.Model):
    note = models.CharField(max_length=300)
    # the current datetime will be automatically filled in. This makes the field non-editable. Once the datetime is set, it is fixed
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(
        Restaurant, related_name='reviews', on_delete=models.CASCADE)
    stars = models.IntegerField(default=5, choices=((i, i)
                                for i in range(1, 6)))
    expenses = models.IntegerField(
        default=5, validators=[MinValueValidator(1), MaxValueValidator(100000)])
    visit_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.note
