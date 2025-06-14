from django.shortcuts import render
from basic_app.forms import EnquiryForm
from .models import Enquiry

def index(request):
    return render(request, 'basic_app/index.html')

def enquiry_form_view(request):
    if request.method == 'POST':
        form = EnquiryForm(request.POST)
        if form.is_valid():
            # Picking data intered by user
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            text = form.cleaned_data['text']
            print('Form Validated')
            print("Name: " + name)
            print("email: " + email)
            print("text: " + text)
            Enquiry.objects.create(name=name, email=email, text=text)
            
            return render(request, 'basic_app/form_page.html', {'form': EnquiryForm(),
                          'success': True
                          })
        else:
            print('Form Invalid')
            # form_filled = EnquiryForm()
    else:
        form = EnquiryForm()
    return render(request, 'basic_app/form_page.html', {'form': form})