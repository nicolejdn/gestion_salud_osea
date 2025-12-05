from django.db import models

class Especialista(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    especialidad = models.CharField(max_length=100)
    matricula_profesional = models.CharField(max_length=50, unique=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    
    def __str__(self):
        return f"{self.nombre} {self.apellido} ({self.especialidad})"


class Paciente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    rut = models.CharField(max_length=20, unique=True, blank=True, null=True)
    fecha_nacimiento = models.DateField()
    genero = models.CharField(max_length=10)
    direccion = models.CharField(max_length=255, blank=True, null=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(unique=True)
    especialistas = models.ManyToManyField(
        'Especialista',
        blank=True,
        related_name='pacientes_asignados'
    )
    
    def __str__(self):
        return f"Paciente: {self.nombre} {self.apellido}"

class PacienteEspecialista(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    especialista = models.ForeignKey(Especialista, on_delete=models.CASCADE)
    fecha_asignacion = models.DateField()

    class Meta:
        unique_together = (('paciente', 'especialista'),)

    def __str__(self):
        return f"{self.paciente.nombre} asignado a {self.especialista.nombre}"

class Diagnostico(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, related_name='diagnosticos')
    tipo_enfermedad = models.CharField(max_length=50)
    nivel_gravedad = models.CharField(max_length=20, blank=True, null=True)
    fecha_diagnostico = models.DateField(auto_now_add=True, verbose_name="Fecha del Diagnóstico")
    
    def __str__(self):
        return f"Diagnóstico de {self.paciente.nombre}: {self.tipo_enfermedad}"

class Tratamiento(models.Model):
    diagnostico = models.ForeignKey(Diagnostico, on_delete=models.CASCADE, related_name='tratamientos')
    tipo_terapia = models.CharField(max_length=100)
    duracion_semanas = models.IntegerField(blank=True, null=True)
    dosis_medicamento = models.CharField(max_length=150, blank=True, null=True)

    def __str__(self):
        return f"Tratamiento: {self.tipo_terapia}"

class Seguimiento(models.Model):
    tratamiento = models.ForeignKey(Tratamiento, on_delete=models.CASCADE, related_name='seguimientos')
    fecha_control = models.DateField()
    observaciones = models.TextField(blank=True, null=True)
    resultado_mejora = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)

    def __str__(self):
        return f"Control de {self.tratamiento.tipo_terapia} en {self.fecha_control}"

class Examen(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, related_name='examenes')
    tipo_examen = models.CharField(max_length=100)
    fecha_examen = models.DateField()
    valor_t_score = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    angulo_cobb = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    url_documento = models.URLField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"Examen de {self.tipo_examen} para {self.paciente.nombre}"
