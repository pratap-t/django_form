from django.shortcuts import render
from basic_app import forms

def index(request):
    return render(request, 'basic_app/index.html')

def form_name_view(request):
    my_form = forms.FormName()
    return render(request, 'basic_app/form_page.html', {'form': my_form})