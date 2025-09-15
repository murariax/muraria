from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            "class": "form-control rounded-lg p-2 bg-gray-100 border border-gray-300",
            "placeholder": "Your Name"
        })
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            "class": "form-control rounded-lg p-2 bg-gray-100 border border-gray-300",
            "placeholder": "Your Email"
        })
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={
            "class": "form-control rounded-lg p-2 bg-gray-100 border border-gray-300",
            "placeholder": "Your Message"
        })
    )
