from django.urls import path
from . import views

urlpatterns = [
    path('api/machines/', views.CoffeMachineList.as_view(), name="machine"),
    path('api/pods/', views.CoffePodsList.as_view(), name="machine"),


]
