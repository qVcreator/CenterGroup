import os

from django.shortcuts import render
from django.core.mail import EmailMessage

from django.views.generic import FormView

from .forms import LeaveRequestForm
from .models import *


def main_page(request):
    apartments = Apartment.objects.all()
    comments = Comment.objects.all()
    message = ""
    if request.method == 'POST':
        form = LeaveRequestForm(request.POST)
        if form.is_valid():
            user_name = form.cleaned_data.get("Name")
            user_phone = form.cleaned_data.get("PhoneNumber")
            user_mail = form.cleaned_data.get("Email")

            body = f'Добрый день, меня зовут {user_name}!\nПрошу связаться со мной по почте ({user_mail}) или по телефону {user_phone} '
            email = EmailMessage(f'Консультация-{user_name}', body, to=[os.environ['EMAIL_TO']])
            email.send()

            message = "Ваш запрос отправлен"
    else:
        form = LeaveRequestForm()

    context = {
        'apartments': apartments,
        'form': form,
        'message': message,
        'comments': comments
    }

    return render(request, 'landing/home.html', context=context)


def apartment_page(request):
    context = {
        # content later
    }
    return render(request, 'landing/apartment.html', context=context)
