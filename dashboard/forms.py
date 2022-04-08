from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import DateInput

from .models import *


class NotesForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ['title', 'description']


class DateInput(forms.DateInput):
    input_type = 'date'


class HomeworkForm(forms.ModelForm):
    class Meta:
        model = Homework
        widgets = {'due_date': DateInput()}
        fields = ['subject', 'title', 'description', 'due_date', 'is_finished']


class DashboardForm(forms.Form):
    text = forms.CharField(max_length=100, label='Enter your search')


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'is_finished']


class ConversionForm(forms.Form):
    CHOISES = [('lenght', 'Length'), ('mass', 'Mass')]
    measurement = forms.ChoiceField(choices=CHOISES, widget=forms.RadioSelect)


class ConversionLengthForm(forms.Form):
    CHOISES = [('yard', 'Yard'), ('foot', 'Foot')]
    input = forms.CharField(required=False, label=False, widget=forms.TextInput(
        attrs={'type': 'number', 'placeholder': 'Enter your Number'}))
    measure1 = forms.CharField(
        label='', widget=forms.Select(choices=CHOISES))
    measure2 = forms.CharField(
        label='', widget=forms.Select(choices=CHOISES))


class ConversionMassForm(forms.Form):
    CHOISES = [('pound', 'Pound'), ('kilogram', 'Kilogram')]
    input = forms.CharField(required=False, label=False, widget=forms.TextInput(
        attrs={'type': 'number', 'placeholder': 'Enter your Number'}))
    measure1 = forms.CharField(
        label='', widget=forms.Select(choices=CHOISES))
    measure2 = forms.CharField(
        label='', widget=forms.Select(choices=CHOISES))


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
