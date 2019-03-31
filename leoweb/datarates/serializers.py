from rest_framework import serializers
from .models import Datarate

class DatarateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Datarate
        fields = '__all__'
        # fields = ('dr',)