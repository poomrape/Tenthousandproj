from django import forms

class LocationForm(forms.Form):
    location = forms.CharField(max_length=255, required=False, widget=forms.TextInput(attrs={'placeholder': 'Enter location'}))

class RadiusForm(forms.Form):
    radius = forms.CharField(max_length=255, required=False, widget=forms.TextInput(attrs={'placeholder': 'Radius:m.'}))