# from dataclasses import field
from rest.models import Stud
from rest_framework import serializers
# from rest_framework.serializers import Serializer



class StudSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stud
        fields = ['name', 'age', 'city']
