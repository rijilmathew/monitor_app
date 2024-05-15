# urls.py
from django.urls import path
from .views import CriteriaListCreateAPIView, CriteriaRetrieveUpdateDestroyAPIView,WeatherDataAPIView

urlpatterns = [
    path('criteria/', CriteriaListCreateAPIView.as_view(), name='criteria-list-create'),
    path('criteria/<int:pk>/', CriteriaRetrieveUpdateDestroyAPIView.as_view(), name='criteria-detail'),
    path('weather/<str:parameter>/', WeatherDataAPIView.as_view(), name='weather-data'),
]
