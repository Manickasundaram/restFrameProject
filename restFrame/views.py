from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import APIView
from .serializers import postSerializers
from rest_framework.viewsets import ModelViewSet
from .models import restFramePost

# Create your views here.

class restFrameView(APIView):

    def get(self,request):
        return Response({'info':'Hello world'})

class postView(ModelViewSet):
    queryset = restFramePost.objects.all()
    serializer_class = postSerializers