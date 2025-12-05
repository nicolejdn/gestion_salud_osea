from django.urls import path
from . import views
from django.contrib.auth.views import LoginView

urlpatterns = [
    # Módulo Pacientes
    path('', views.lista_pacientes, name='lista_pacientes'),
    path('nuevo/', views.crear_paciente, name='crear_paciente'),
    path('<int:pk>/', views.detalle_paciente, name='detalle_paciente'),
    path('<int:pk>/editar/', views.editar_paciente, name='editar_paciente'),
    path('pacientes/<int:pk>/eliminar/', views.eliminar_paciente, name='eliminar_paciente'),

    

    # Login
    path("cuentas/login/", LoginView.as_view(), name="login"),

    # API
    path('api/v1/pacientes/', views.paciente_list_api, name='paciente-list-api'),
    path('api/v1/pacientes/<int:pk>/', views.paciente_detail_api, name='paciente-detail-api'),

    # --- ESPECIALISTAS ---
path('especialistas/', views.lista_especialistas, name='lista_especialistas'),
path('especialistas/nuevo/', views.crear_especialista, name='crear_especialista'),
path('especialistas/<int:pk>/', views.detalle_especialista, name='detalle_especialista'),
path('especialistas/<int:pk>/editar/', views.editar_especialista, name='editar_especialista'),
path('especialistas/<int:pk>/eliminar/', views.eliminar_especialista, name='eliminar_especialista'),

# --- DIAGNÓSTICOS ---
path('diagnosticos/', views.lista_diagnosticos, name='lista_diagnosticos'),
path('diagnosticos/nuevo/', views.crear_diagnostico, name='crear_diagnostico'),
path('diagnosticos/<int:pk>/', views.detalle_diagnostico, name='detalle_diagnostico'),
path('diagnosticos/<int:pk>/editar/', views.editar_diagnostico, name='editar_diagnostico'),
path('diagnosticos/<int:pk>/eliminar/', views.eliminar_diagnostico, name='eliminar_diagnostico'),

# --- TRATAMIENTOS ---
path('tratamientos/', views.lista_tratamientos, name='lista_tratamientos'),
path('tratamientos/nuevo/', views.crear_tratamiento, name='crear_tratamiento'),
path('tratamientos/<int:pk>/', views.detalle_tratamiento, name='detalle_tratamiento'),
path('tratamientos/<int:pk>/editar/', views.editar_tratamiento, name='editar_tratamiento'),
path('tratamientos/<int:pk>/eliminar/', views.eliminar_tratamiento, name='eliminar_tratamiento'),

# --- SEGUIMIENTOS ---
path('seguimientos/', views.lista_seguimientos, name='lista_seguimientos'),
path('seguimientos/nuevo/', views.crear_seguimiento, name='crear_seguimiento'),
path('seguimientos/<int:pk>/', views.detalle_seguimiento, name='detalle_seguimiento'),
path('seguimientos/<int:pk>/editar/', views.editar_seguimiento, name='editar_seguimiento'),
path('seguimientos/<int:pk>/eliminar/', views.eliminar_seguimiento, name='eliminar_seguimiento'),

# --- EXÁMENES ---
path('examenes/', views.lista_examenes, name='lista_examenes'),
path('examenes/nuevo/', views.crear_examen, name='crear_examen'),
path('examenes/<int:pk>/', views.detalle_examen, name='detalle_examen'),
path('examenes/<int:pk>/editar/', views.editar_examen, name='editar_examen'),
path('examenes/<int:pk>/eliminar/', views.eliminar_examen, name='eliminar_examen'),


]






