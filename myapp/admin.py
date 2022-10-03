from django.contrib import admin
from .models import MainCategoryModel,SubCategoryModel
# Register your models here.


@admin.register(MainCategoryModel)
class MainCategoryModelAdmin(admin.ModelAdmin):
    list_display = ["name"]


@admin.register(SubCategoryModel)
class SubCategoryModelAdmin(admin.ModelAdmin):
    list_display = ["maincategory","name",]
