from django.contrib import admin
from .models import Paciente, Especialista, Diagnostico, Tratamiento, Seguimiento, Examen, PacienteEspecialista

class DiagnosticoInline(admin.TabularInline):
    model = Diagnostico
    extra = 1
    fields = ('tipo_enfermedad', 'nivel_gravedad', 'fecha_diagnostico')

class ExamenInline(admin.TabularInline):
    model = Examen
    extra = 1
    fields = ('tipo_examen', 'fecha_examen', 'valor_t_score', 'angulo_cobb')

class PacienteEspecialistaInline(admin.TabularInline):
    model = PacienteEspecialista
    extra = 1

class PacienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'fecha_nacimiento', 'email')
    search_fields = ('nombre', 'apellido', 'email')
    inlines = [PacienteEspecialistaInline, DiagnosticoInline, ExamenInline]

class TratamientoInline(admin.TabularInline):
    model = Tratamiento
    extra = 1

class DiagnosticoAdmin(admin.ModelAdmin):
    list_display = ('paciente', 'tipo_enfermedad', 'nivel_gravedad', 'fecha_diagnostico')
    list_filter = ('tipo_enfermedad', 'nivel_gravedad')
    inlines = [TratamientoInline]

admin.site.register(Especialista)
admin.site.register(Paciente, PacienteAdmin)
admin.site.register(Diagnostico, DiagnosticoAdmin)
admin.site.register(Tratamiento)
admin.site.register(Seguimiento)
admin.site.register(Examen)
