#/MainApp/management/commands/create_sample_data.py
from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import time, timedelta, datetime
from random import choice, randint, random
from ...models import (
    Establecimiento, ConfiguracionHorario, Curso, Apoderado,
    Estudiante, HuellaDigital, Atraso, Inasistencia, Notificacion
)

class Command(BaseCommand):
    help = 'Creates sample data for testing'

    def handle(self, *args, **kwargs):
        self.stdout.write('Creating sample data...')
        
        # Create Establecimiento
        establecimiento = Establecimiento.objects.create(
            nombre="Colegio San José",
            hora_entrada_regular=time(8, 0)  # 8:00 AM
        )
        
        # Create ConfiguracionHorario
        dias = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes']
        for dia in dias:
            ConfiguracionHorario.objects.create(
                establecimiento=establecimiento,
                hora_entrada=time(8, 0),
                limite_atraso=time(8, 30),
                dia_semana=dia
            )
        
        # Create Cursos
        cursos = []
        niveles = ['1°', '2°', '3°', '4°']
        tipos = ['Básico', 'Medio']
        for nivel in niveles:
            for tipo in tipos:
                curso = Curso.objects.create(
                    nombre=f"{nivel} {tipo}",
                    nivel=tipo,
                    establecimiento=establecimiento
                )
                cursos.append(curso)
        
        # Create Apoderados first
        apoderados = []
        nombres = ["Juan", "María", "Pedro", "Ana", "Carlos", "Laura"]
        apellidos = ["González", "Rodríguez", "Pérez", "López", "Martínez", "Silva"]
        
        # Create 20 apoderados
        for i in range(20):
            apoderado = Apoderado.objects.create(
                rut=f"{randint(10000000, 25000000)}-{randint(0, 9)}",
                nombre=f"{choice(nombres)} {choice(apellidos)}",
                telefono=f"+569{randint(10000000, 99999999)}",
                email=f"apoderado{i}@example.com",
                preferencia_notificacion=choice(['SMS', 'Email', 'WhatsApp'])
            )
            apoderados.append(apoderado)
        
        # Create 50 Estudiantes
        estudiantes = []
        for i in range(50):
            estudiante = Estudiante.objects.create(
                rut=f"{randint(10000000, 25000000)}-{randint(0, 9)}",
                nombre=choice(nombres),
                apellidos=f"{choice(apellidos)} {choice(apellidos)}",
                curso=choice(cursos),
                apoderado=choice(apoderados),  # Now one apoderado can have multiple students
                activo=random() > 0.1  # 90% active
            )
            estudiantes.append(estudiante)
        
        # Create HuellaDigital
        for estudiante in estudiantes:
            HuellaDigital.objects.create(
                estudiante=estudiante,
                template_huella=b'sample_fingerprint_template',
                fecha_registro=timezone.now().date() - timedelta(days=randint(0, 365))
            )
        
        # Create Atrasos
        for _ in range(100):
            estudiante = choice(estudiantes)
            fecha = timezone.now().date() - timedelta(days=randint(0, 30))
            hora_llegada = datetime.combine(fecha, time(8, randint(1, 59)))
            
            Atraso.objects.create(
                estudiante=estudiante,
                hora_llegada=hora_llegada,
                justificacion="Problema de transporte" if random() > 0.5 else None,
                justificado=random() > 0.7,
                fecha=fecha
            )
        
        # Create Inasistencias
        for _ in range(80):
            estudiante = choice(estudiantes)
            fecha = timezone.now().date() - timedelta(days=randint(0, 30))
            
            Inasistencia.objects.create(
                estudiante=estudiante,
                fecha=fecha,
                justificacion="Enfermedad" if random() > 0.5 else None,
                justificada=random() > 0.6,
                tipo_inasistencia=choice(['Día Completo', 'Media Jornada'])
            )
        
        # Create Notificaciones
        tipos_registro = ['atraso', 'inasistencia']
        estados = ['Enviado', 'Entregado', 'Leído', 'Fallido']
        
        for _ in range(150):
            estudiante = choice(estudiantes)
            tipo = choice(tipos_registro)
            fecha_envio = timezone.now() - timedelta(days=randint(0, 30))
            
            if tipo == 'atraso':
                mensaje = "Su pupilo ha llegado atrasado al establecimiento."
            else:
                mensaje = "Su pupilo no ha asistido al establecimiento."
            
            Notificacion.objects.create(
                registro_id=randint(1, 100),
                tipo_registro=tipo,
                apoderado=estudiante.apoderado,
                fecha_envio=fecha_envio,
                estado=choice(estados),
                mensaje=mensaje
            )

        self.stdout.write(self.style.SUCCESS('Sample data created successfully'))