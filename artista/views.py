from django.shortcuts import render
from django.http import Http404
from rest_framework import viewsets, views
from artista.models import Artista
from artista.serializers import ArtistaSerializer, ArtistaLightSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.authentication import TokenAuthentication
from rest_framework.filters import SearchFilter
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

class ArtistaViewSet(viewsets.ModelViewSet):
    filter_backends = [SearchFilter]
    search_fields = ['^nome', '=idade']
    queryset = Artista.objects.all()
    # permission_classes = (IsAuthenticatedOrReadOnly,)
    # authentication_classes = (TokenAuthentication,)
    serializer_class = ArtistaSerializer

class ArtistaList(views.APIView):
    def get(self, request):
        artista = Artista.objects.all()
        serializer = ArtistaLightSerializer(artista, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self,request):
        serializer = ArtistaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ArtistaDetails(views.APIView):
    
    def get_object(self, id):
        try:
            return Artista.objects.get(id=id)
        except:
            raise Http404
    
    def get(self, request, id):
        artista = self.get_object(id)
        serializer = ArtistaSerializer(artista)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request,id):
        artista = self.get_object(id)
        serializer = ArtistaSerializer(artista, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)