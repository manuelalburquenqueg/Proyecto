from django_filters import rest_framework as filters
from .models import Estudiante, Atraso, Inasistencia

class EstudianteFilter(filters.FilterSet):
    nombre = filters.CharFilter(lookup_expr='icontains')
    apellidos = filters.CharFilter(lookup_expr='icontains')
    rut = filters.CharFilter(lookup_expr='iexact')
    curso = filters.NumberFilter(field_name='curso_id')
    activo = filters.BooleanFilter()
    
    class Meta:
        model = Estudiante
        fields = ['nombre', 'apellidos', 'rut', 'curso', 'activo']

class AtrasoFilter(filters.FilterSet):
    fecha_inicio = filters.DateFilter(field_name='fecha', lookup_expr='gte')
    fecha_fin = filters.DateFilter(field_name='fecha', lookup_expr='lte')
    justificado = filters.BooleanFilter()
    estudiante = filters.NumberFilter(field_name='estudiante_id')
    
    class Meta:
        model = Atraso
        fields = ['fecha_inicio', 'fecha_fin', 'justificado', 'estudiante']

class InasistenciaFilter(filters.FilterSet):
    fecha_inicio = filters.DateFilter(field_name='fecha', lookup_expr='gte')
    fecha_fin = filters.DateFilter(field_name='fecha', lookup_expr='lte')
    justificado = filters.BooleanFilter()
    estudiante = filters.NumberFilter(field_name='estudiante_id')
    
    class Meta:
        model = Inasistencia
        fields = ['fecha_inicio', 'fecha_fin', 'justificado', 'estudiante']