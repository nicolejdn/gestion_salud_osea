# C:\Proyectoapp\salud_osea\apps.py

from django.apps import AppConfig

class SaludOseaConfig(AppConfig):
    # Asegúrate de que este nombre sea correcto (salud_osea)
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'salud_osea'
    verbose_name = 'Gestión de Salud Ósea' # Nombre amigable
