from rest_framework import serializers
from .models import (
    Establecimiento, ConfiguracionHorario, Curso, Apoderado,
    Estudiante, HuellaDigital, Atraso, Inasistencia, Notificacion
)

class EstablecimientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Establecimiento
        fields = '__all__'

class ConfiguracionHorarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConfiguracionHorario
        fields = '__all__'

class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'

class ApoderadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Apoderado
        fields = '__all__'

class EstudianteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudiante
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['curso'] = CursoSerializer(instance.curso).data
        representation['apoderado'] = ApoderadoSerializer(instance.apoderado).data
        return representation

class HuellaDigitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = HuellaDigital
        fields = '__all__'

class AtrasoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Atraso
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['estudiante'] = EstudianteSerializer(instance.estudiante).data
        return representation

class InasistenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inasistencia
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['estudiante'] = EstudianteSerializer(instance.estudiante).data
        return representation

class NotificacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notificacion
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['apoderado'] = ApoderadoSerializer(instance.apoderado).data
        return representation