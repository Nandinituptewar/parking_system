from django.shortcuts import render
from rest_framework import viewsets
from .serializers import MovieSerializer,RatingSerializer,UserSerializer
from .models import Rating,Movie
from rest_framework.response import Response
from rest_framework import status
from .models import Movie
from rest_framework.decorators import action
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication
# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class MovieViewSet(viewsets.ModelViewSet):
    serializer_class = MovieSerializer
    queryset =Movie.objects.all()

    authentication_classes = (TokenAuthentication,)


    @action(detail=True,methods=['POST'])

    def rate_movie(self,request,pk=None):
        if 'stars' in  request.data:
            movie=Movie.objects.get(id=pk)
            #print(pk)    whatever will be sent in url  will be pk. http://127.0.0.1:8000/api/movie/2/rate_movie/ here pk=2
            stars=request.data['stars']
            user=request.user
            print('user',user)
            user=User.objects.get(id=1)

            try:
                rating=Rating.objects.get(user=user.id,movie=movie.id)
                rating.stars=stars
                rating.save()
                serializer=RatingSerializer(rating,many=False)
                response = {"msg": "Rating Updated" ,'result':serializer.data}
                return Response(response,status=status.HTTP_200_OK)
            except:
                rating=Rating.objects.create(user=user,movie=movie,stars=stars)
                serializer=RatingSerializer(rating,many=False)
                response={'message':'rating created','result':serializer.data}
                return Response(response, status=status.HTTP_200_OK)
        else:
            response={'message':'You need to provide stars'}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)


class RatingViewset(viewsets.ModelViewSet):
    serializer_class = RatingSerializer
    queryset=Rating.objects.all()
    authentication_classes = (TokenAuthentication,)