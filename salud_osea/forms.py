from django import forms
from .models import (
    Paciente, Especialista, Diagnostico,
    Tratamiento, Seguimiento, Examen
)

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = '__all__'

class DiagnosticoForm(forms.ModelForm):
    class Meta:
        model = Diagnostico
        fields = ['paciente', 'tipo_enfermedad', 'nivel_gravedad']


class EspecialistaForm(forms.ModelForm):
    class Meta:
        model = Especialista
        fields = '__all__'

class TratamientoForm(forms.ModelForm):
    class Meta:
        model = Tratamiento
        fields = '__all__'


class SeguimientoForm(forms.ModelForm):
    class Meta:
        model = Seguimiento
        fields = '__all__'


class ExamenForm(forms.ModelForm):
    class Meta:
        model = Examen
        fields = '__all__'
