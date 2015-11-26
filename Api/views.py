from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ColegioSerialerzs,EstudianteSerialerzs,DocenteSerialerzs,PuntuacionSerialerzs,UsuarioSerialerzs
from .models import *
from django.shortcuts import get_object_or_404
# Create your views here.
class ColegioApi(APIView):
    serializer_class = ColegioSerialerzs

    def get(self,request,cod=None,format=None):
        muchos = False
        if cod != None:
            colegio = get_object_or_404(Colegio,pk=cod)
        else:
            muchos = True
            colegio = Colegio.objects.all()
        response = self.serializer_class(colegio,many=muchos)
        return Response(response.data)

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, cod, format=None):
        colegio =  get_object_or_404(Colegio,pk=cod)
        serializer = self.serializer_class(colegio, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, cod, format=None):
        colegio = get_object_or_404(Colegio,pk=cod)
        colegio.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class EstudianteApi(APIView):
    serializer_class = EstudianteSerialerzs
    def get(self,request,ced=None,format=None):
        muchos = False
        if ced != None:
            estudiante = get_object_or_404(Estudiante,pk=ced)
        else:
            muchos = True
            estudiante= Estudiante.objects.all()
        response=self.serializer_class(estudiante,many=muchos)
        return Response(response.data)

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, ced, format=None):
        estudiante =  get_object_or_404(Estudiante,pk=ced)
        serializer = self.serializer_class(estudiante, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, ced, format=None):
        estudiante = get_object_or_404(Estudiante,pk=ced)
        estudiante.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class DocenteApi(APIView):
    serializer_class = DocenteSerialerzs
    def get(self,request,ced=None,format=None):
        muchos = False
        if ced != None:
            docente=get_object_or_404(Docente,pk=ced)
        else:
            muchos = True
            docente= Docente.objects.all()
        response = self.serializer_class(docente,many=muchos)
        return Response(response.data)

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, ced, format=None):
        docente =  get_object_or_404(Docente,pk=ced)
        serializer = self.serializer_class(docente, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, ced, format=None):
        docente = get_object_or_404(Docente,pk=ced)
        docente.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PuntuacionApi(APIView):
    serializer_class= PuntuacionSerialerzs
    def get(self,request,cod=None,format=None):
        muchos = False
        if cod != None:
            puntuacion= get_object_or_404(Puntuacion,pk=cod)
        else:
            muchos = True
            puntuacion= Puntuacion.objects.all()
        response=self.serializer_class(puntuacion,many=muchos)
        return Response(response.data)

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, cod, format=None):
        puntuacion =  get_object_or_404(Puntuacion,pk=cod)
        serializer = self.serializer_class(puntuacion, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, cod, format=None):
        puntuacion = get_object_or_404(Puntuacion,pk=cod)
        puntuacion.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

