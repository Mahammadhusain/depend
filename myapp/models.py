from django.db import models

# Create your models here.
class MainCategoryModel(models.Model):
    name = models.CharField(max_length=100)

    objects = models.Manager()

    def __str__(self):
        return self.name

class SubCategoryModel(models.Model):
    maincategory = models.ForeignKey(MainCategoryModel,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    objects = models.Manager()

    def __str__(self):
        return self.name