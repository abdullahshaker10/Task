from django.shortcuts import render
from .serializers import CoffeMachineSerializer, CoffePodsSerializer
from .models import CoffeMachine, CoffePods
from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend


class CoffeMachineList(ListAPIView):
    serializer_class = CoffeMachineSerializer
    queryset = CoffeMachine.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('product_type', 'model', 'water_line_compatible')


class CoffePodsList(ListAPIView):
    serializer_class = CoffePodsSerializer
    queryset = CoffePods.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('product_type', 'coffe_flavor', 'pack_size',)
