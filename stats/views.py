from django.shortcuts import render
from .models import MaxTemp
from rest_framework import generics, response
from .serializers import MaxTempSerializer

# ViewSets define the view behavior.
class MaxTempViewAll(generics.ListAPIView):
    """Get annual values of Max Temp by year order.
    """
    
    queryset = MaxTemp.objects.all()
    serializer_class = MaxTempSerializer

class MaxTempFilter(generics.ListAPIView):
    """Get annual values of Max Temp by year order filtered by city name.
    """
    queryset = MaxTemp.objects.all()
    def list(self, request, filter):
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = MaxTemp.objects.filter(city=filter)
        print(queryset)
        serializer = MaxTempSerializer(queryset, many=True)
        return response.Response(serializer.data)
