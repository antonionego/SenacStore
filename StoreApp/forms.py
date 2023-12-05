from django import forms

class ContatoForm(forms.Form):

    nome = forms.CharField()
    email = forms.EmailField()
    telefone = forms.CharField(widget=forms.TextInput)
    assunto = forms.CharField()
    mensagem = forms.CharField(widget=forms.Textarea)