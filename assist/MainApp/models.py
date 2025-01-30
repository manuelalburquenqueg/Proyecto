from django.db import models

# Create your models here.
class task (models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    done = models.BooleanField(default=False)

class Establecimiento(models.Model):
    nombre = models.CharField(max_length=200)
    hora_entrada_regular = models.TimeField()

    def __str__(self):
        return self.nombre

class ConfiguracionHorario(models.Model):
    establecimiento = models.ForeignKey(Establecimiento, on_delete=models.CASCADE, related_name='configuraciones_horario')
    hora_entrada = models.TimeField()
    limite_atraso = models.TimeField()
    dia_semana = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.establecimiento.nombre} - {self.dia_semana}"

class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    nivel = models.CharField(max_length=50)
    establecimiento = models.ForeignKey(Establecimiento, on_delete=models.PROTECT, related_name='cursos')

    def __str__(self):
        return f"{self.nombre} - {self.nivel}"

class Apoderado(models.Model):
    rut = models.CharField(max_length=20, unique=True)
    nombre = models.CharField(max_length=200)
    telefono = models.CharField(max_length=20)
    email = models.EmailField()
    preferencia_notificacion = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nombre} ({self.rut})"

class Estudiante(models.Model):
    rut = models.CharField(max_length=20, unique=True)
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=200)
    curso = models.ForeignKey(Curso, on_delete=models.PROTECT, related_name='estudiantes')
    apoderado = models.ForeignKey(Apoderado, on_delete=models.PROTECT, related_name='estudiantes')
    activo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nombre} {self.apellidos} ({self.rut})"

class HuellaDigital(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE, related_name='huellas_digitales')
    template_huella = models.BinaryField()
    fecha_registro = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Huella de {self.estudiante.nombre} {self.estudiante.apellidos}"

class Atraso(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.SET_NULL,null=True, related_name='atrasos')
    hora_llegada = models.DateTimeField()
    justificacion = models.TextField(blank=True, null=True)
    justificado = models.BooleanField(default=False)
    fecha = models.DateField()

    def __str__(self):
        return f"Atraso de {self.estudiante.nombre} - {self.fecha}"

class Inasistencia(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.SET_NULL, null=True, related_name='inasistencias')
    fecha = models.DateField()
    justificacion = models.TextField(blank=True, null=True)
    justificada = models.BooleanField(default=False)
    tipo_inasistencia = models.CharField(max_length=50)

    def __str__(self):
        return f"Inasistencia de {self.estudiante.nombre} - {self.fecha}"

class Notificacion(models.Model):
    registro_id = models.IntegerField()
    tipo_registro = models.CharField(max_length=50)  # 'atraso' or 'inasistencia'
    apoderado = models.ForeignKey(Apoderado, on_delete=models.CASCADE, related_name='notificaciones')
    fecha_envio = models.DateTimeField()
    estado = models.CharField(max_length=50)
    mensaje = models.TextField()

    def __str__(self):
        return f"Notificación para {self.apoderado.nombre} - {self.fecha_envio}"