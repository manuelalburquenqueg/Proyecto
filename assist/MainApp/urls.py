from django.urls import path, include ,re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.routers import DefaultRouter
from .views import (
    EstablecimientoViewSet, ConfiguracionHorarioViewSet,
    CursoViewSet, ApoderadoViewSet, EstudianteViewSet,
    HuellaDigitalViewSet, AtrasoViewSet, InasistenciaViewSet,
    NotificacionViewSet
)

router = DefaultRouter()
router.register(r'establecimientos', EstablecimientoViewSet)
router.register(r'configuraciones-horario', ConfiguracionHorarioViewSet)
router.register(r'cursos', CursoViewSet)
router.register(r'apoderados', ApoderadoViewSet)
router.register(r'estudiantes', EstudianteViewSet)
router.register(r'huellas-digitales', HuellaDigitalViewSet)
router.register(r'atrasos', AtrasoViewSet)
router.register(r'inasistencias', InasistenciaViewSet)
router.register(r'notificaciones', NotificacionViewSet)


schema_view = get_schema_view(
    openapi.Info(
        title="API de Atrasos en Colegios",
        default_version='v1',
        description="API para administrar atrasos, asistencia escolar y registros estudiantiles.",
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    # API URLs
    path('api/', include(router.urls)),
    
    # Swagger URLs
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', 
            schema_view.without_ui(cache_timeout=0), 
            name='schema-json'),
    path('swagger/', 
         schema_view.with_ui('swagger', cache_timeout=0), 
         name='schema-swagger-ui'),
    path('redoc/', 
         schema_view.with_ui('redoc', cache_timeout=0), 
         name='schema-redoc'),
]