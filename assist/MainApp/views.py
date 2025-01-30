from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import (
    Establecimiento, ConfiguracionHorario, Curso, Apoderado,
    Estudiante, HuellaDigital, Atraso, Inasistencia, Notificacion
)
from .serializers import (
    EstablecimientoSerializer, ConfiguracionHorarioSerializer,
    CursoSerializer, ApoderadoSerializer, EstudianteSerializer,
    HuellaDigitalSerializer, AtrasoSerializer, InasistenciaSerializer,
    NotificacionSerializer
)
from .filters import (EstudianteFilter,AtrasoFilter,InasistenciaFilter)

class EstablecimientoViewSet(viewsets.ModelViewSet):
    queryset = Establecimiento.objects.all()
    serializer_class = EstablecimientoSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=True, methods=['get'])
    def get_cursos(self, request, pk=None):
        establecimiento = self.get_object()
        cursos = Curso.objects.filter(establecimiento=establecimiento)
        serializer = CursoSerializer(cursos, many=True)
        return Response(serializer.data)

class ConfiguracionHorarioViewSet(viewsets.ModelViewSet):
    queryset = ConfiguracionHorario.objects.all()
    serializer_class = ConfiguracionHorarioSerializer
    permission_classes = [IsAuthenticated]

class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=True, methods=['get'])
    def get_estudiantes(self, request, pk=None):
        curso = self.get_object()
        estudiantes = Estudiante.objects.filter(curso=curso)
        serializer = EstudianteSerializer(estudiantes, many=True)
        return Response(serializer.data)

class ApoderadoViewSet(viewsets.ModelViewSet):
    queryset = Apoderado.objects.all()
    serializer_class = ApoderadoSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=True, methods=['get'])
    def get_estudiantes(self, request, pk=None):
        apoderado = self.get_object()
        estudiantes = Estudiante.objects.filter(apoderado=apoderado)
        serializer = EstudianteSerializer(estudiantes, many=True)
        return Response(serializer.data)

class EstudianteViewSet(viewsets.ModelViewSet):
    queryset = Estudiante.objects.all()
    serializer_class = EstudianteSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_class = EstudianteFilter
    search_fields = ['nombre', 'apellidos', 'rut']
    ordering_fields= ['nombre', 'apellidos','curso__nombre']
    permission_classes = [IsAuthenticated]

    @action(detail=True, methods=['get'])
    def get_atrasos(self, request, pk=None):
        estudiante = self.get_object()
        atrasos = Atraso.objects.filter(estudiante=estudiante)
        serializer = AtrasoSerializer(atrasos, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['get'])
    def get_inasistencias(self, request, pk=None):
        estudiante = self.get_object()
        inasistencias = Inasistencia.objects.filter(estudiante=estudiante)
        serializer = InasistenciaSerializer(inasistencias, many=True)
        return Response(serializer.data)

class HuellaDigitalViewSet(viewsets.ModelViewSet):
    queryset = HuellaDigital.objects.all()
    serializer_class = HuellaDigitalSerializer
    permission_classes = [IsAuthenticated]

class AtrasoViewSet(viewsets.ModelViewSet):
    queryset = Atraso.objects.all()
    serializer_class = AtrasoSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_class = AtrasoFilter
    ordering_fields = ['fecha', 'hora_llegada']
    permission_classes = [IsAuthenticated]

class InasistenciaViewSet(viewsets.ModelViewSet):
    queryset = Inasistencia.objects.all()
    serializer_class = InasistenciaSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_class = InasistenciaFilter
    ordering_fields = ['fecha', 'hora_llegada']
    permission_classes = [IsAuthenticated]

class NotificacionViewSet(viewsets.ModelViewSet):
    queryset = Notificacion.objects.all()
    serializer_class = NotificacionSerializer
    permission_classes = [IsAuthenticated]