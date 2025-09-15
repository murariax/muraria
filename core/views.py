from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from .forms import ContactForm
from django.conf import settings
from django.urls import reverse

# Create your views here.
def home(request):
    return render(request, "core/home.html")

def about(request):
    return render(request, "core/about.html")

def projects(request):
    return render(request, "core/projects.html")

def contact_success(request):
    name = request.GET.get("name", "")
    return render(request, "core/contact_success.html", {"name": name})



def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            message = form.cleaned_data["message"]

            subject = f"New Contact Form Submission from {name}"
            body = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"

            email_message = EmailMessage(
                subject=subject,
                body=body,
                from_email=settings.DEFAULT_FROM_EMAIL,  # your Gmail
                to=[settings.RECIPIENT_ADDRESS],         # where you want to receive
                reply_to=[email],  # 👈 ensures you can reply directly to sender
            )
            email_message.send()

            return redirect(f"{reverse('contact_success')}?name={name}")

    else:
        form = ContactForm()
    return render(request, "core/contact.html", {"form": form})
    

