import os

from django.shortcuts import render, get_object_or_404
from django.core.mail import EmailMessage

from django.views.generic import FormView, TemplateView, DetailView

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

    def post(self, request, *args, **kwargs):
        context = self.get_context_data()

        apartments = Apartment.objects.all()
        comments = Comment.objects.all()
        comment_form = CommentForm(request.POST)
        feedback_form = FeedbackForm(request.POST)

        context['apartments'] = apartments
        context['comments'] = comments
        context['feedback_form'] = feedback_form
        context['comment_form'] = comment_form

        if 'comm_btn' in request.POST:
            if comment_form.is_valid():
                comment_form.save()
                return self.render_to_response(context)
            else:
                context['message'] = "Проверьте введенные данные"
                return self.render_to_response(context)

        if 'cons_btn' in request.POST:
            if feedback_form.is_valid():
                # feedback_form.save()

                send_email(feedback_form)

                return self.render_to_response(context)
            else:
                context['message'] = "Проверьте введенные данные"
                return self.render_to_response(context)


# def apartment_page(request, apartment_id: int):
#     apartment = Apartment.objects.filter(id=apartment_id)
#     return render(request, 'landing/apartment.html', {'apartment': apartment})

class ApartmentPage(TemplateView):
    template_name = 'landing/apartment.html'

    def get(self, request, *args, **kwargs):
        ap_id = self.kwargs['apartment_id']

        ap = get_object_or_404(Apartment, id=ap_id)
        photos = list(ApartmentPhotos.objects.all().filter(apartment=ap_id))

        context = self.get_context_data(**kwargs)
        context['ap'] = ap
        context['photos'] = photos

        return self.render_to_response(context)


def send_email(form: FeedbackForm):
    user_name = form.cleaned_data.get("Name")
    user_phone = form.cleaned_data.get("PhoneNumber")
    user_mail = form.cleaned_data.get("Email")

    body = f'Добрый день, меня зовут {user_name}!\nПрошу связаться со мной по почте ({user_mail}) или по телефону {user_phone} '
    email = EmailMessage(f'Консультация-{user_name}', body, to=[os.environ['EMAIL_TO']])
    email.send()
