from django.shortcuts import render


def main_page(request):
    context = {
        # content later
    }
    return render(request, 'landing/home.html', context=context)


def apartment_page(request):
    context = {
        # content later
    }
    return render(request, 'landing/apartment.html', context=context)
