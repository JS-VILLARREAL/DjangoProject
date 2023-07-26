from django import forms

class CreateNewTask(forms.Form):
    title = forms.CharField(label='Title', max_length=100, widget=forms.TextInput(attrs={'class': 'input'}))
    description = forms.CharField(label='Description Task', widget=forms.Textarea(attrs={'class': 'input'}))

class CreateProject(forms.Form):
    name = forms.CharField(label='Name Project', max_length=200, widget=forms.TextInput(attrs={'class': 'input'}))