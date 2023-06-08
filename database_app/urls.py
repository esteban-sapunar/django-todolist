from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path("<int:id>",views.list,name="list"),
    path('create/',views.create,name="create"),
]