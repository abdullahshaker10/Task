from rest_framework import serializers
from .models import CoffeMachine, CoffePods


class CoffeMachineSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoffeMachine
        fields = '__all__'


class CoffePodsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoffePods
        fields = '__all__'
