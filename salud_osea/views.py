from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.db import IntegrityError

from .models import Paciente
from .forms import PacienteForm

# API REST
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import PacienteSerializer


# =======================================================
# VISTAS WEB (MVT)
# =======================================================

@login_required
def lista_pacientes(request):
    pacientes = Paciente.objects.all()
    return render(request, "salud_osea/lista_pacientes.html", {"pacientes": pacientes})


@login_required
def detalle_paciente(request, pk):
    paciente = get_object_or_404(Paciente, pk=pk)
    return render(request, "salud_osea/detalle_paciente.html", {"paciente": paciente})


@login_required
def crear_paciente(request):
    if request.method == "POST":
        form = PacienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("lista_pacientes")
    else:
        form = PacienteForm()

    return render(request, "salud_osea/crear_paciente.html", {"form": form})


@login_required
def editar_paciente(request, pk):
    paciente = get_object_or_404(Paciente, pk=pk)

    if request.method == "POST":
        form = PacienteForm(request.POST, instance=paciente)
        if form.is_valid():
            form.save()
            return redirect("detalle_paciente", pk=paciente.pk)
    else:
        form = PacienteForm(instance=paciente)

    return render(request, "salud_osea/editar_paciente.html", {
        "form": form,
        "paciente": paciente
    })


@login_required
@require_POST
def eliminar_paciente(request, pk):
    paciente = get_object_or_404(Paciente, pk=pk)
    paciente.delete()
    return redirect('lista_pacientes')


# =======================================================
# API REST
# =======================================================

@api_view(["GET", "POST"])
def paciente_list_api(request):
    if request.method == "GET":
        pacientes = Paciente.objects.all()
        serializer = PacienteSerializer(pacientes, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = PacienteSerializer(data=request.data)
        if serializer.is_valid():
            try:
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            except IntegrityError:
                return Response({"error": "Datos duplicados o inválidos"},
                                status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
def paciente_detail_api(request, pk):
    try:
        paciente = Paciente.objects.get(pk=pk)
    except Paciente.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = PacienteSerializer(paciente)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = PacienteSerializer(paciente, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        paciente.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

from .forms import (
    PacienteForm, EspecialistaForm, DiagnosticoForm,
    TratamientoForm, SeguimientoForm, ExamenForm
)
from .models import (
    Paciente, Especialista, Diagnostico,
    Tratamiento, Seguimiento, Examen
)

@login_required
def lista_especialistas(request):
    especialistas = Especialista.objects.all()
    return render(request, "salud_osea/lista_especialistas.html", {"especialistas": especialistas})


@login_required
def crear_especialista(request):
    if request.method == "POST":
        form = EspecialistaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("lista_especialistas")
    else:
        form = EspecialistaForm()
    return render(request, "salud_osea/crear_especialista.html", {"form": form})


@login_required
def detalle_especialista(request, pk):
    especialista = get_object_or_404(Especialista, pk=pk)
    return render(request, "salud_osea/detalle_especialista.html", {"especialista": especialista})


@login_required
def editar_especialista(request, pk):
    especialista = get_object_or_404(Especialista, pk=pk)
    if request.method == "POST":
        form = EspecialistaForm(request.POST, instance=especialista)
        if form.is_valid():
            form.save()
            return redirect("detalle_especialista", pk=pk)
    else:
        form = EspecialistaForm(instance=especialista)
    return render(request, "salud_osea/editar_especialista.html", {"form": form})


@login_required
@require_POST
def eliminar_especialista(request, pk):
    especialista = get_object_or_404(Especialista, pk=pk)
    especialista.delete()
    return redirect("lista_especialistas")

@login_required
def lista_diagnosticos(request):
    diagnosticos = Diagnostico.objects.all()
    return render(request, "salud_osea/lista_diagnosticos.html", {"diagnosticos": diagnosticos})


@login_required
def crear_diagnostico(request):
    if request.method == "POST":
        form = DiagnosticoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("lista_diagnosticos")
    else:
        form = DiagnosticoForm()
    return render(request, "salud_osea/crear_diagnostico.html", {"form": form})


@login_required
def detalle_diagnostico(request, pk):
    diagnostico = get_object_or_404(Diagnostico, pk=pk)
    return render(request, "salud_osea/detalle_diagnostico.html", {"diagnostico": diagnostico})


@login_required
def editar_diagnostico(request, pk):
    diagnostico = get_object_or_404(Diagnostico, pk=pk)
    if request.method == "POST":
        form = DiagnosticoForm(request.POST, instance=diagnostico)
        if form.is_valid():
            form.save()
            return redirect("detalle_diagnostico", pk=pk)
    else:
        form = DiagnosticoForm(instance=diagnostico)
    return render(request, "salud_osea/editar_diagnostico.html", {"form": form})


@login_required
@require_POST
def eliminar_diagnostico(request, pk):
    diagnostico = get_object_or_404(Diagnostico, pk=pk)
    diagnostico.delete()
    return redirect("lista_diagnosticos")

@login_required
def lista_tratamientos(request):
    tratamientos = Tratamiento.objects.all()
    return render(request, "salud_osea/lista_tratamientos.html", {"tratamientos": tratamientos})


@login_required
def crear_tratamiento(request):
    if request.method == "POST":
        form = TratamientoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("lista_tratamientos")
    else:
        form = TratamientoForm()
    return render(request, "salud_osea/crear_tratamiento.html", {"form": form})


@login_required
def detalle_tratamiento(request, pk):
    tratamiento = get_object_or_404(Tratamiento, pk=pk)
    return render(request, "salud_osea/detalle_tratamiento.html", {"tratamiento": tratamiento})


@login_required
def editar_tratamiento(request, pk):
    tratamiento = get_object_or_404(Tratamiento, pk=pk)
    if request.method == "POST":
        form = TratamientoForm(request.POST, instance=tratamiento)
        if form.is_valid():
            form.save()
            return redirect("detalle_tratamiento", pk=pk)
    else:
        form = TratamientoForm(instance=tratamiento)
    return render(request, "salud_osea/editar_tratamiento.html", {"form": form})


@login_required
@require_POST
def eliminar_tratamiento(request, pk):
    tratamiento = get_object_or_404(Tratamiento, pk=pk)
    tratamiento.delete()
    return redirect("lista_tratamientos")

@login_required
def lista_seguimientos(request):
    seguimientos = Seguimiento.objects.all()
    return render(request, "salud_osea/lista_seguimientos.html", {"seguimientos": seguimientos})


@login_required
def crear_seguimiento(request):
    if request.method == "POST":
        form = SeguimientoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("lista_seguimientos")
    else:
        form = SeguimientoForm()
    return render(request, "salud_osea/crear_seguimiento.html", {"form": form})


@login_required
def detalle_seguimiento(request, pk):
    seguimiento = get_object_or_404(Seguimiento, pk=pk)
    return render(request, "salud_osea/detalle_seguimiento.html", {"seguimiento": seguimiento})


@login_required
def editar_seguimiento(request, pk):
    seguimiento = get_object_or_404(Seguimiento, pk=pk)
    if request.method == "POST":
        form = SeguimientoForm(request.POST, instance=seguimiento)
        if form.is_valid():
            form.save()
            return redirect("detalle_seguimiento", pk=pk)
    else:
        form = SeguimientoForm(instance=seguimiento)
    return render(request, "salud_osea/editar_seguimiento.html", {"form": form})


@login_required
@require_POST
def eliminar_seguimiento(request, pk):
    seguimiento = get_object_or_404(Seguimiento, pk=pk)
    seguimiento.delete()
    return redirect("lista_seguimientos")

@login_required
def lista_examenes(request):
    examenes = Examen.objects.all()
    return render(request, "salud_osea/lista_examenes.html", {"examenes": examenes})


@login_required
def crear_examen(request):
    if request.method == "POST":
        form = ExamenForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("lista_examenes")
    else:
        form = ExamenForm()
    return render(request, "salud_osea/crear_examen.html", {"form": form})


@login_required
def detalle_examen(request, pk):
    examen = get_object_or_404(Examen, pk=pk)
    return render(request, "salud_osea/detalle_examen.html", {"examen": examen})


@login_required
def editar_examen(request, pk):
    examen = get_object_or_404(Examen, pk=pk)
    if request.method == "POST":
        form = ExamenForm(request.POST, instance=examen)
        if form.is_valid():
            form.save()
            return redirect("detalle_examen", pk=pk)
    else:
        form = ExamenForm(instance=examen)
    return render(request, "salud_osea/editar_examen.html", {"form": form})


@login_required
@require_POST
def eliminar_examen(request, pk):
    examen = get_object_or_404(Examen, pk=pk)
    examen.delete()
    return redirect("lista_examenes")
