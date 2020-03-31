from django.shortcuts import render

# Create your views here.
from django.shortcuts import get_object_or_404
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from Profile.models import Perfil
from Profile.models import ModelEstado
from Profile.models import ModelCiudad
from Profile.models import ModelGenero
from Profile.models import ModelOcupacion
from Profile.models import ModelEstadoCivil
from rest_framework.authtoken.views import ObtainAuthToken
from Profile.serializer import PerfilSerializers
from Profile.serializer import EstadoCivilSerializers
from Profile.serializer import CiudadSerializers
from Profile.serializer import EstadoSerializers
from Profile.serializer import OcupacionSerializers
from Profile.serializer import GeneroSerializers
import coreapi
from rest_framework.schemas import AutoSchema

class CustonAuthToken(ObtainAuthToken):
    
    def post(self, request, * args, **kwars):
        serializer = self.serializer_class (data = request.data, 
                                            context = {
                                                    'request': request, 
                                                    }
                                            )
        serializer.is_valid(raise_exception = True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)

        return Response({
            'token': token.key,
            'user_id': user.pk,
            'username': user.username
        })

class PerfilListViewSchema(AutoSchema):
    def get_manual_fields(self,path,method):
        extra_fields = []
        if method.lower() in ('post','get'):
            extra_fields = [
                coreapi.Field('nombre')
            ]
        manual_fields =super().get_manual_fields(path,method)
        return manual_fields + extra_fields


class PerfilList(APIView):
    permission_classes = []
    schema = PerfilListViewSchema()
    def get(self, request, format=None):
        print("Metodo get filter")
        queryset = Perfil.objects.filter(delete = False)
        serializer = PerfilSerializers(queryset,many=True)
        return Response(serializer.data)

    def post(self,request,format=None):
        serializer = PerfilSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas =serializer.data
            return Response(datas)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


class EstadoList(APIView):
    permission_classes = []
    schema = PerfilListViewSchema()
    def get(self, request, format=None):
        print("Metodo get filter")
        queryset = ModelEstado.objects.filter(delete = False)
        serializer = EstadoSerializers(queryset,many=True)
        return Response(serializer.data)

    def post(self,request,format=None):
        serializer = EstadoSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas =serializer.data
            return Response(datas)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


class GeneroList(APIView):
    permission_classes = []
    schema = PerfilListViewSchema()
    def get(self, request, format=None):
        print("Metodo get filter")
        queryset = ModelGenero.objects.filter(delete = False)
        serializer = GeneroSerializers(queryset,many=True)
        return Response(serializer.data)

    def post(self,request,format=None):
        serializer = GeneroSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas =serializer.data
            return Response(datas)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        
class CiudadList(APIView):
    permission_classes = []
    schema = PerfilListViewSchema()
    def get(self, request, format=None):
        print("Metodo get filter")
        queryset = ModelCiudad.objects.filter(delete = False)
        serializer = CiudadSerializers(queryset,many=True)
        return Response(serializer.data)

    def post(self,request,format=None):
        serializer = CiudadSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas =serializer.data
            return Response(datas)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class EstadoCivilList(APIView):
    permission_classes = []
    schema = PerfilListViewSchema()
    def get(self, request, format=None):
        print("Metodo get filter")
        queryset = ModelEstadoCivil.objects.filter(delete = False)
        serializer = EstadoCivilSerializers(queryset,many=True)
        return Response(serializer.data)

    def post(self,request,format=None):
        serializer = EstadoCivilSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas =serializer.data
            return Response(datas)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class OcupacionList(APIView):
    permission_classes = []
    schema = PerfilListViewSchema()
    def get(self, request, format=None):
        print("Metodo get filter")
        queryset = ModelOcupacion.objects.filter(delete = False)
        serializer = OcupacionSerializers(queryset,many=True)
        return Response(serializer.data)

    def post(self,request,format=None):
        serializer = OcupacionSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas =serializer.data
            return Response(datas)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)