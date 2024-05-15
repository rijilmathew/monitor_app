from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import requests
from django.conf import settings
from .models import Criteria, WeatherData
from .serializers import CriteriaSerializer, WeatherDataSerializer



class CriteriaListCreateAPIView(generics.ListCreateAPIView):
    queryset = Criteria.objects.all()
    serializer_class = CriteriaSerializer



class CriteriaRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Criteria.objects.all()
    serializer_class = CriteriaSerializer

#check the 

class WeatherDataAPIView(APIView):
    def get_weather_data(self, api_key):
        url = f"https://api.openweathermap.org/data/2.5/weather?q=kerala&appid={api_key}"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            return None
    
    def get_threshold_value(self, parameter):
        try:
            criteria = Criteria.objects.get(parameter=parameter)
            return criteria.threshold
        except Criteria.DoesNotExist:
            return None
    
    def celsius_to_kelvin(self, celsius):
        return celsius + 273.15
    
    def get(self, request,parameter):
        threshold_celsius = self.get_threshold_value(parameter)
        if threshold_celsius is None:
            return Response({'message': 'No temperature threshold data found'}, status=status.HTTP_404_NOT_FOUND)
        
        api_response = self.get_weather_data(settings.API_KEY)

        api_temp_max_kelvin = api_response.get('main', {}).get('temp_max')

        if api_temp_max_kelvin is None:
            return Response({'message': 'No temperature data found in API response'}, status=status.HTTP_404_NOT_FOUND)

        threshold_kelvin = self.celsius_to_kelvin(threshold_celsius)

        if api_temp_max_kelvin > threshold_kelvin:
            WeatherData.objects.create(parameter=parameter, value=api_temp_max_kelvin)
            return Response({'message': 'Heatwave detected!'}, status=status.HTTP_200_OK)
        else:
            WeatherData.objects.create(parameter=parameter, value=api_temp_max_kelvin)
            return Response({'message': 'No heatwave detected'}, status=status.HTTP_200_OK)
