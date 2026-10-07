from django import forms

from models import Professor

class ProfessorForm(forms.ModelForm):
    class Meta:
        model = Professor
        fields = ['nome', 'sobrenome', 'email', 'telefone', 'registro',]

# ERRO ENCONTRADO: descrição clara do que estava errado
# CORREÇÃO:        o que foi alterado e por quê