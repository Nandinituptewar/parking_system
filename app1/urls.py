from django.urls import path, include
from . import views
from rest_framework import routers
from .views import PersonViewSet
from .views import line_chart, line_chart_json

router=routers.DefaultRouter()
router.register('Person',PersonViewSet)
urlpatterns = [
    path('',include(router.urls)),
    path('home/', views.HomeView.as_view(), name='home-page'),
    path('form/', views.FormView_1.as_view(), name='form-page'),
    path('datadisplay/', views.TableView.as_view(), name='TableView-page'),
    path('finish_form/', views.Finish_entry.as_view(), name='finish-page'),
    path('parking_finish/', views.parking_finish.as_view(), name='parking-finish'),
    path('forget_id/', views.forget_password.as_view(), name='forget_password'),
    path('chart/', line_chart, name='line_chart'),
    path('chartJSON/', line_chart_json, name='line_chart_json'),
]
