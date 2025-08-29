from django.shortcuts import render
from django.core.mail import send_mail
from .forms import ContactForm

# Create your views here.
def home(request):
    return render(request, "core/home.html")

def about(request):
    return render(request, "core/about.html")

def projects(request):
    return render(request, "core/projects.html")

def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            # Process the form data (e.g., send an email)
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            # Here you would typically send the email or save the message
            return render(request, "core/contact.html", {"form": ContactForm(), "success": True})
    else:
        form = ContactForm()

    return render(request, "core/contact.html", {"form": form})
    

