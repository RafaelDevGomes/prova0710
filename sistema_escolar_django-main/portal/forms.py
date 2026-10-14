from django import forms

from .models import Professor

class ProfessorForm(forms.ModelForm):
    class Meta:
        model = Professor
        fields = ['nome', 'sobrenome', 'email', 'telefone', 'registro',]

# ERRO ENCONTRADO: Erro no models e no import.
# CORREÇÃO:        O ponto na frente do models para reconhecer a classe Professor.