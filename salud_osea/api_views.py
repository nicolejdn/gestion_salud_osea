from rest_framework import viewsets
from .models import (
    Paciente,
    Especialista,
    PacienteEspecialista,
    Diagnostico,
    Tratamiento,
    Seguimiento,
    Examen
)
from .serializers import (
    PacienteSerializer,
    EspecialistaSerializer,
    PacienteEspecialistaSerializer,
    DiagnosticoSerializer,
    TratamientoSerializer,
    SeguimientoSerializer,
    ExamenSerializer
)

class PacienteViewSet(viewsets.ModelViewSet):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer


class EspecialistaViewSet(viewsets.ModelViewSet):
    queryset = Especialista.objects.all()
    serializer_class = EspecialistaSerializer


class PacienteEspecialistaViewSet(viewsets.ModelViewSet):
    queryset = PacienteEspecialista.objects.all()
    serializer_class = PacienteEspecialistaSerializer


class DiagnosticoViewSet(viewsets.ModelViewSet):
    queryset = Diagnostico.objects.all()
    serializer_class = DiagnosticoSerializer


class TratamientoViewSet(viewsets.ModelViewSet):
    queryset = Tratamiento.objects.all()
    serializer_class = TratamientoSerializer


class SeguimientoViewSet(viewsets.ModelViewSet):
    queryset = Seguimiento.objects.all()
    serializer_class = SeguimientoSerializer


class ExamenViewSet(viewsets.ModelViewSet):
    queryset = Examen.objects.all()
    serializer_class = ExamenSerializer
