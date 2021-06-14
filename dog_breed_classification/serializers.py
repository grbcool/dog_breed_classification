from rest_framework import serializers
from .models import dogimage
from drf_extra_fields.fields import Base64ImageField

'''
class dogimageserializer(serializers.ModelSerializer):
    image = Base64ImageField()
    class Meta:
        model = dogimage
        fields = ['image']
'''         
