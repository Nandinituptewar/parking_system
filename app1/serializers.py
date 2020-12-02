from rest_framework import serializers

from .models import Person,park_area_data,slot_description

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ('id', 'name', 'plate_num', 'status', 'time_1')

