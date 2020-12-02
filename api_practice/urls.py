from django.urls import path, include
from rest_framework import routers
from .views import MovieViewSet,RatingViewset,UserViewSet
router=routers.DefaultRouter()
router.register('movie',MovieViewSet)
router.register('rating',RatingViewset)
router.register('users',UserViewSet)


urlpatterns = [
    path('',include(router.urls)),
]


