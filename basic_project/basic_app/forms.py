from django import forms
from django.core import validators
from basic_app.models import Enquiry

class EnquiryForm(forms.ModelForm):
    class Meta():
        model = Enquiry
        fields = '__all__'

def start_with_a(value):
    if value[0].lower() != 'a':
        raise forms.ValidationError('Name should start with "A"')

class FormName(forms.Form):
    name = forms.CharField(validators=[start_with_a])
    email = forms.EmailField(disabled=False)
    text = forms.CharField(widget=forms.Textarea, max_length=100)
    rob_catcher = forms.CharField(required=False, widget=forms.HiddenInput,
                                  validators=[validators.MaxLengthValidator(0)])

    def clean_rob_catcher(self):
        rob_catcher = self.cleaned_data['rob_catcher']
        if len(rob_catcher)>0:
            raise forms.ValidationError('Robot Found')
        return rob_catcher