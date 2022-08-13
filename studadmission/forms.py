from django import forms
from studadmission.models import StudAdmission


class StudAdmissionForm(forms.ModelForm):
    class Meta:
        model = StudAdmission
        fields = '__all__'
