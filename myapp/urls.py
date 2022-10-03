from django.urls import path
from .views import index,sub
urlpatterns = [
    path('',index,name='index'),
    path('sub/',sub,name='sub'),
]
