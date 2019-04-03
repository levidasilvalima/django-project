from rest_framework import serializers

from .models import Unicorn

class UnicornSerializer(serializers.ModelSerializer):

    class Meta: 
        model = Unicorn
        fields = ('name', 'age')