from django import forms

from .models import Patient

from datetime import date


class PatientForm(forms.ModelForm):

    class Meta:

        model = Patient

        fields = "__all__"

    def clean_dob(self):

        dob = self.cleaned_data["dob"]

        if dob > date.today():

            raise forms.ValidationError(

                "Future DOB not allowed"

            )

        return dob

    def clean_glucose(self):

        glucose = self.cleaned_data["glucose"]

        if glucose < 0:

            raise forms.ValidationError(

                "Invalid glucose value"

            )

        return glucose