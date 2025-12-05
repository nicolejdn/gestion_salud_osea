from rest_framework import serializers
from .models import Paciente, Especialista
from .models import (
    Paciente,
    Especialista,
    PacienteEspecialista,
    Diagnostico,
    Tratamiento,
    Seguimiento,
    Examen
)

# =============================
#  ESPECIALISTA
# =============================
class EspecialistaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Especialista
        fields = '__all__'


# =============================
#  PACIENTE
# =============================
class PacienteSerializer(serializers.ModelSerializer):
    especialistas = EspecialistaSerializer(many=True, read_only=True)

    class Meta:
        model = Paciente
        fields = '__all__'


# =============================
#  PACIENTE-ESPECIALISTA (TABLA INTERMEDIA)
# =============================
class PacienteEspecialistaSerializer(serializers.ModelSerializer):
    paciente = PacienteSerializer(read_only=True)
    especialista = EspecialistaSerializer(read_only=True)

    class Meta:
        model = PacienteEspecialista
        fields = '__all__'


# =============================
#  DIAGNÓSTICO
# =============================
class DiagnosticoSerializer(serializers.ModelSerializer):
    paciente = serializers.PrimaryKeyRelatedField(queryset=Paciente.objects.all())

    class Meta:
        model = Diagnostico
        fields = '__all__'


# =============================
#  TRATAMIENTO
# =============================
class TratamientoSerializer(serializers.ModelSerializer):
    diagnostico = serializers.PrimaryKeyRelatedField(queryset=Diagnostico.objects.all())

    class Meta:
        model = Tratamiento
        fields = '__all__'


# =============================
#  SEGUIMIENTO
# =============================
class SeguimientoSerializer(serializers.ModelSerializer):
    tratamiento = serializers.PrimaryKeyRelatedField(queryset=Tratamiento.objects.all())

    class Meta:
        model = Seguimiento
        fields = '__all__'


# =============================
#  EXAMEN
# =============================
class ExamenSerializer(serializers.ModelSerializer):
    paciente = serializers.PrimaryKeyRelatedField(queryset=Paciente.objects.all())

    class Meta:
        model = Examen
        fields = '__all__'

