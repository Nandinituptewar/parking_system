from rest_framework import serializers
from .models import Movie,Rating
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['id','username','password']
        extra_kwargs={'password':{'write_only':True,'required':True}}

        def create(self,validated_data):
            user1=User.objects.create_user(**validated_data)
            token=Token.objects.create(user=user1)
            return user1

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model=Movie
        fields=['id','title','description','no_of_ratings','avg_ratings']
        #fields = '__all__'

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model=Rating
        #field=['movie','user','rating',]
        fields = '__all__'
