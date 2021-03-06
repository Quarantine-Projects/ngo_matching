from rest_framework import serializers
from .models import NGO

class NGOSerializer(serializers.ModelSerializer):
    class Meta:
        model = NGO
        fields = ('id', 'name','full_address', 'contact_1', 'contact_2', 'website', 'email')

class CreateNGOSerializer(serializers.ModelSerializer):
    class Meta:
        model = NGO
        fields = "__all__"