from django.forms import ModelForm
from django import forms

from administrativo.models import Estudiante, \
        NumeroTelefonico


class EstudianteForm(ModelForm):
    class Meta:
        model = Estudiante
        fields = ['nombre', 'apellido', 'cedula']


class NumeroTelefonicoForm(ModelForm):
    class Meta:
        model = NumeroTelefonico
        fields = ['telefono', 'tipo', 'estudiante']


class NumeroTelefonicoEstudianteForm(ModelForm):

    def __init__(self, estudiante, *args, **kwargs):
        super(NumeroTelefonicoEstudianteForm, self).__init__(*args, **kwargs)
        self.initial['estudiante'] = estudiante
        self.fields["estudiante"].widget = forms.widgets.HiddenInput()
        print(estudiante)

    class Meta:
        model = NumeroTelefonico
        fields = ['telefono', 'tipo', 'estudiante']

