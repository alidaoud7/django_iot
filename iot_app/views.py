from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import SensorDataSerializer
from .models import SensorData
class SensorDataView(APIView):
    def get(self, request, format=None):
        # Retrieve all sensor data entries
        sensor_data = SensorData.objects.all()
        serializer = SensorDataSerializer(sensor_data, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        # Create a new sensor data entry
        serializer = SensorDataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
