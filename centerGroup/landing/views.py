import os

from django.shortcuts import render
from django.core.mail import EmailMessage
from django.urls import reverse_lazy

from django.views.generic import FormView, TemplateView

from .forms import *
from .models import *


class MainPageView(TemplateView):
    template_name = 'landing/home.html'

    def get(self, request, *args, **kwargs):
        apartments = Apartment.objects.all()
        comments = Comment.objects.all()

        feedback_form = FeedbackForm(self.request.GET or None)
        comment_form = CommentForm(self.request.GET or None)

        context = self.get_context_data(**kwargs)
        context['apartments'] = apartments
        context['comments'] = comments
        context['feedback_form'] = feedback_form
        context['comment_form'] = comment_form

        return self.render_to_response(context)


def apartment_page(request):
    context = {
        # content later
    }
    return render(request, 'landing/apartment.html', context=context)


class FeedbackFormView(FormView):
    form_class = FeedbackForm
    template_name = 'landing/home.html'
    success_url = reverse_lazy('home')

    def post(self, request, *args, **kwargs):
        feedback_form = self.form_class(request.POST)
        if feedback_form.is_valid():
            feedback_form.save()

            user_name = feedback_form.cleaned_data.get("Name")
            user_phone = feedback_form.cleaned_data.get("PhoneNumber")
            user_mail = feedback_form.cleaned_data.get("Email")

            body = f'Добрый день, меня зовут {user_name}!\nПрошу связаться со мной по почте ({user_mail}) или по телефону {user_phone} '
            email = EmailMessage(f'Консультация-{user_name}', body, to=[os.environ['EMAIL_TO']])
            email.send()
            
            return self.render_to_response(
                self.get_context_data(
                    message="Ваш запрос отправлен"
                )
            )
        else:
            return self.render_to_response(
                self.get_context_data(
                    message="Проверьте введенные данные"
                )
            )


class CommentFormView(FormView):
    form_class = CommentForm
    template_name = 'landing/home.html'
    success_url = reverse_lazy('home')

    def post(self, request, *args, **kwargs):
        comment_form = self.form_class(request.POST)
        if comment_form.is_valid():
            comment_form.save()
            return self.render_to_response(
                self.get_context_data(
                    success=True
                )
            )
        else:
            return self.render_to_response(
                self.get_context_data(
                    message="Проверьте введенные данные"
                )
            )
