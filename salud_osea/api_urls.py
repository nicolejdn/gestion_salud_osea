from rest_framework.routers import DefaultRouter
from .api_views import (
    PacienteViewSet,
    EspecialistaViewSet,
    PacienteEspecialistaViewSet,
    DiagnosticoViewSet,
    TratamientoViewSet,
    SeguimientoViewSet,
    ExamenViewSet
)

router = DefaultRouter()
router.register('pacientes', PacienteViewSet)
router.register('especialistas', EspecialistaViewSet)
router.register('paciente-especialista', PacienteEspecialistaViewSet)
router.register('diagnosticos', DiagnosticoViewSet)
router.register('tratamientos', TratamientoViewSet)
router.register('seguimientos', SeguimientoViewSet)
router.register('examenes', ExamenViewSet)

urlpatterns = router.urls
