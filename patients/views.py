from django.shortcuts import render, redirect

from .models import Patient

from .forms import PatientForm

from .predictor import health_prediction


def patient_list(request):

    patients = Patient.objects.all()

    return render(

        request,

        "patient_list.html",

        {"patients": patients}

    )


def add_patient(request):

    form = PatientForm(

        request.POST or None

    )

    if form.is_valid():

        patient = form.save(

            commit=False

        )

        patient.remarks = health_prediction(

            patient.glucose,

            patient.haemoglobin,

            patient.cholesterol

        )

        patient.save()

        return redirect(

            "list"

        )

    return render(

        request,

        "add_patient.html",

        {"form": form}

    )

def update_patient(request, id):
    
    patient = Patient.objects.get(id=id)

    form = PatientForm(

        request.POST or None,

        instance=patient

    )

    if form.is_valid():

        patient = form.save(commit=False)

        patient.remarks = health_prediction(

            patient.glucose,

            patient.haemoglobin,

            patient.cholesterol

        )

        patient.save()

        return redirect('list')

    return render(

        request,

        'add_patient.html',

        {'form': form}

    )


def delete_patient(request, id):

    patient = Patient.objects.get(id=id)

    patient.delete()

    return redirect('list')