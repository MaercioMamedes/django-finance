from django.shortcuts import render, redirect
from apps.core.forms.contactForm import ContactForm


def contact(request):
    if request.method == 'POST':

        form = ContactForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('index')

    form = ContactForm()

    return render(request, 'core/contact.html', {'form': form})
