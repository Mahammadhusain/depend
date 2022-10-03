from django.shortcuts import render
from .models import MainCategoryModel,SubCategoryModel
# Create your views here.
def index(request):
    dropone = MainCategoryModel.objects.all()
    context = {'dropone':dropone}
    return render(request,'index.html',context)

def sub(request):
    mainid = request.GET.get('maincategory')
    droptwo = SubCategoryModel.objects.filter(maincategory_id = mainid)
    context = {'droptwo':droptwo}
    return render(request,'subcategory.html',context)