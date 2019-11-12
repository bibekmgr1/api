from django.shortcuts import render
from .serializers import HouseDetailsSerializer
from .models import HouseDetails
from datetime import datetime
from rest_framework import generics
from django.http import JsonResponse

# Create your views here.

class CreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = HouseDetails.objects.all()
    serializer_class = HouseDetailsSerializer

    def post(self, request):
        save = request.POST.get ('time')
        # get time as string for example suppose on request we get time value as given:
        # then convert time string to time object of python
        # time_object = datetime.strptime(time_str, '%H::%M::%S').time()
        time_object = datetime.strptime(save, '%H::%M::%S')
        start = datetime.time([8, 0, 0])
        end = datetime.time([12, 0, 0])
        serializer = HouseDetailsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        print("is valid")
        print(start)
        print(save)
        print(end)
        if start <= save <= end:
            return JsonResponse({
                'status': 'True'
            })
        else:
            return JsonResponse({
                'status': 'False'
            })
    def perform_create(self, serializer):
        """Save the post data when creating a new bucketlist."""
        serializer.save()


class DetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""

    queryset = HouseDetails.objects.all()
    serializer_class = HouseDetailsSerializer



