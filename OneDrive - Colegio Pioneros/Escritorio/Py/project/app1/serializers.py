from rest_framework import serializers
from .models import bd_raw_data_old, bd_raw_data_new

class BdRawDataOldSerializer(serializers.ModelSerializer):
    class Meta:
        model = bd_raw_data_old
        fields = '__all__'

class BdRawDataNewSerializer(serializers.ModelSerializer):
    class Meta:
        model = bd_raw_data_new
        fields = '__all__'
