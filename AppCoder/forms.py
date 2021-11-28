from django import forms

class FutbolistasFormulario(forms.Form):
    nombre = forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'form-control' , 'autocomplete': 'off','pattern':'[A-Za-z,á,Á,é,É,í,Í,ó,Ó,ú,Ú,ñ,Ñ]+', 'title':'Solo se permiten letras'}))
    apellido =forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'form-control' , 'autocomplete': 'off','pattern':'[A-Za-z,á,Á,é,É,í,Í,ó,Ó,ú,Ú,ñ,Ñ]+', 'title':'Solo se permiten letras'}))
    edad = forms.IntegerField(required=True,widget=forms.TextInput(attrs={'class':'form-control' , 'autocomplete': 'off','pattern':'[0-9 ]+', 'title':'Solo se permiten números'}))
    
class BasquetbolistasFormulario(forms.Form):
    nombre = forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'form-control' , 'autocomplete': 'off','pattern':'[A-Za-z,á,Á,é,É,í,Í,ó,Ó,ú,Ú,ñ,Ñ]+', 'title':'Solo se permiten letras'}))
    apellido =forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'form-control' , 'autocomplete': 'off','pattern':'[A-Za-z,á,Á,é,É,í,Í,ó,Ó,ú,Ú,ñ,Ñ]+', 'title':'Solo se permiten letras'}))
    triples = forms.IntegerField(required=True,widget=forms.TextInput(attrs={'class':'form-control' , 'autocomplete': 'off','pattern':'[0-9 ]+', 'title':'Solo se permiten números'}))
    
class TenistasFormulario(forms.Form):
    nombre = forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'form-control' , 'autocomplete': 'off','pattern':'[A-Za-z,á,Á,é,É,í,Í,ó,Ó,ú,Ú,ñ,Ñ]+', 'title':'Solo se permiten letras'}))
    apellido =forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'form-control' , 'autocomplete': 'off','pattern':'[A-Za-z,á,Á,é,É,í,Í,ó,Ó,ú,Ú,ñ,Ñ]+', 'title':'Solo se permiten letras'}))
    titulos = forms.IntegerField(required=True,widget=forms.TextInput(attrs={'class':'form-control' , 'autocomplete': 'off','pattern':'[0-9 ]+', 'title':'Solo se permiten números'}))